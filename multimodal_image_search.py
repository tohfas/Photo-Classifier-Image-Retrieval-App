from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes.retriever.multimodal import MultiModalRetriever
import os
from haystack import Document
from haystack import Pipeline

class MultimodalSearch:
    def __init__(self):
        # Initialise the DocumentStore to store 512 dim image embeddings
        self.document_store = InMemoryDocumentStore(embedding_dim=512)

        # Specify the directory where the images are stored
        data_path = "tmp/images"

        # Load images from the directory and wrap them as Haystack Document objects
        images = [
            Document(content=f"./{data_path}/{filename}", content_type="image")
            for filename in os.listdir(f"./{data_path}")
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))  # Ensure only image files are processed
        ]

        # Write the documents (images) into the DocumentStore
        self.document_store.write_documents(images)

        # Initialise the MultiModalRetriever with a pre-trained CLIP model for text-to-image search
        self.retriever_text_to_image = MultiModalRetriever(
            document_store=self.document_store,
            query_embedding_model="sentence-transformers/clip-ViT-B-32",
            query_type="text",
            document_embedding_models={"image": "sentence-transformers/clip-ViT-B-32"},
        )

        # Generate embeddings for all the images and store them in the DocumentStore
        self.document_store.update_embeddings(retriever=self.retriever_text_to_image)

        # Set up the pipeline to handle the search flow
        self.pipeline = Pipeline()
        self.pipeline.add_node(component=self.retriever_text_to_image, name="retriever_text_to_image", inputs=["Query"])

    def search_images(self, prompt, top_k=5):
        results = self.pipeline.run(query=prompt, params={"retriever_text_to_image": {"top_k": top_k}})
        
        # Filter results to only include those with a score above a certain threshold (you can adjust this)
        filtered_results = [doc for doc in results["documents"] if doc.score > 0.5]  # Set your score threshold here
        
        # Return top_k results sorted by score
        return sorted(filtered_results, key=lambda d: d.score, reverse=True)[:top_k]