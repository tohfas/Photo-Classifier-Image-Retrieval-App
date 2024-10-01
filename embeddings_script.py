# embedding_script.py
import os
import pickle
from haystack.document_stores import InMemoryDocumentStore
from haystack.nodes.retriever.multimodal import MultiModalRetriever
from haystack import Document

def precompute_image_embeddings(data_path="tmp/images", embedding_file="image_embeddings.pkl"):
    # Initialising the DocumentStore to store 512-dim image embeddings
    document_store = InMemoryDocumentStore(embedding_dim=512)
    
    # Loading images and wrapping them as Haystack Document objects
    images = [Document(content=f"./{data_path}/{filename}", content_type="image") 
              for filename in os.listdir(f"./{data_path}")
              if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    
    # Writing the documents (images) into the DocumentStore
    document_store.write_documents(images)
    
    # Initialising the MultiModalRetriever with a pre-trained CLIP model for text-to-image search
    retriever = MultiModalRetriever(
        document_store=document_store,
        query_embedding_model="sentence-transformers/clip-ViT-B-32",
        query_type="text",
        document_embedding_models={"image": "sentence-transformers/clip-ViT-B-32"},
    )
    
    # Generating and storing embeddings
    document_store.update_embeddings(retriever=retriever)
    
    # Saving the embeddings to disk
    with open(embedding_file, 'wb') as f:
        pickle.dump(document_store, f)
    print(f"Embeddings saved to {embedding_file}")

if __name__ == "__main__":
    precompute_image_embeddings()
