# search_script.py
import pickle
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes.retriever.multimodal import MultiModalRetriever
from haystack import Pipeline

class MultimodalSearch:
    def __init__(self, embedding_file="image_embeddings.pkl"):
        # Loading the precomputed DocumentStore with embeddings
        self.document_store = self.load_document_store(embedding_file)
        
        # Initialising the MultiModalRetriever
        self.retriever_text_to_image = MultiModalRetriever(
            document_store=self.document_store,
            query_embedding_model="sentence-transformers/clip-ViT-B-32",
            query_type="text",
            document_embedding_models={"image": "sentence-transformers/clip-ViT-B-32"},
        )
        
        # Setting up the search pipeline
        self.pipeline = Pipeline()
        self.pipeline.add_node(component=self.retriever_text_to_image, name="retriever_text_to_image", inputs=["Query"])

    def load_document_store(self, embedding_file):
        with open(embedding_file, 'rb') as f:
            document_store = pickle.load(f)
        return document_store

    def search_images(self, prompt, top_k=5):
        # Running the search pipeline
        results = self.pipeline.run(query=prompt, params={"retriever_text_to_image": {"top_k": top_k}})
        # Filtering and returning top results based on score
        return [doc for doc in results["documents"] if doc.score > 0.5][:top_k]
