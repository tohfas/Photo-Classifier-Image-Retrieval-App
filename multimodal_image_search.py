from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes.retriever.multimodal import MultiModalRetriever
import os
from haystack import Document
from haystack import Pipeline

class MultimodalSearch:
    def __init__(self):

        # Initialise the DocumentStore to store 512 dim image embeddings
        # InMemoryDocumentStore is used to hold image and text embeddings in memory
        self.document_store = InMemoryDocumentStore(embedding_dim=512)

        # Specify the directory where the images are stored
        data_path = "tmp/images"

        # Load images from the directory and wrap them as Haystack Document objects
        # Each Document contains the file path to the image and its content type as "image"
        images = [
            Document(content=f"./{data_path}/{filename}", content_type="image")
            for filename in os.listdir(f"./{data_path}")
        ]

        # Write the documents (images) into the DocumentStore
        self.document_store.write_documents(images)

        # Initialise the MultiModalRetriever with a pre-trained CLIP model for text-to-image search
        # - query_embedding_model: used to generate embeddings for text queries
        # - document_embedding_models: a dictionary mapping content types (e.g., image) to embedding models
        self.retriever_text_to_image = MultiModalRetriever(
            document_store=self.document_store,
            query_embedding_model="sentence-transformers/clip-ViT-B-32",
            query_type="text",
            document_embedding_models={"image": "sentence-transformers/clip-ViT-B-32"},
        )

        # Generate embeddings for all the images and store them in the DocumentStore
        # The retriever is used to compute embeddings for documents and store them as part of the index
        self.document_store.update_embeddings(retriever=self.retriever_text_to_image)

        # Set up the pipeline to handle the search flow
        # Add the text-to-image retriever as a node in the pipeline
        self.pipeline = Pipeline()
        self.pipeline.add_node(component=self.retriever_text_to_image, name="retriever_text_to_image", inputs=["Query"])

    # Function to search for the top_k most relevant images based on a text query
    def search_images(self, prompt, top_k=5):
        results = self.pipeline.run(query=prompt, params={"retriever_text_to_image": {"top_k": top_k}})
        return sorted(results["documents"], key=lambda d: d.score, reverse=True)