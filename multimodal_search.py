import pandas as pd
from PIL import Image
import requests
from tqdm.auto import tqdm
from transformers import CLIPProcessor, CLIPModel
import torch
import streamlit as st

class MultimodalSearch:
    def __init__(self, data_file):

        # Loading the photos file from the directory
        self.df_photos = pd.read_csv(data_file, sep='\t')
        photo_ids = self.df_photos['photo_id'][:500]
        self.df_photos = self.df_photos.loc[photo_ids.index, ['photo_id', 'photo_image_url']]
        
        # Loading the CLIP model and processor
        self.model = CLIPModel.from_pretrained('openai/clip-vit-base-patch32')
        self.processor = CLIPProcessor.from_pretrained('openai/clip-vit-base-patch32')
        
        # Preparing the photo URLs for processing
        self.session = requests.Session()
        self.df_photos['photo_image_url'] = self.df_photos['photo_image_url'].apply(
            lambda x: x + "?q=75&fm=jpg&w=200&fit=max"
        )
        
        # Processing images and creating embeddings
        self.create_embeddings()

    def extract_image_features(self, image):
        inputs = self.processor(images=image, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model.get_image_features(**inputs)
        return outputs.squeeze().tolist()

    def create_embeddings(self):
        # Downloading images and creating embeddings
        self.df_photos['photo_embed'] = [
            self.process_image(url) for url in tqdm(self.df_photos['photo_image_url'], total=len(self.df_photos))
        ]
        # Removing rows where image processing failed
        self.df_photos.dropna(subset=['photo_embed'], inplace=True)
        self.embeddings = torch.tensor(self.df_photos['photo_embed'].tolist())
        self.image_urls = self.df_photos['photo_image_url'].tolist()

    def process_image(self, url):
        try:
            response = self.session.get(url, stream=True)
            response.raise_for_status()
            image = Image.open(response.raw)
            return self.extract_image_features(image)
        except requests.RequestException:
            return None

    def search_images(self, prompt, top_k=5):
        # Preprocessing the prompt to create embeddings
        inputs = self.processor(text=[prompt], return_tensors="pt", padding=True)
        prompt_features = self.model.get_text_features(**inputs)

        # Computing cosine similarity
        similarities = torch.nn.functional.cosine_similarity(prompt_features, self.embeddings)

        # Getting the top k most similar images
        top_k_indices = similarities.topk(k=top_k).indices
        results = [(self.image_urls[idx], similarities[idx].item()) for idx in top_k_indices]

        return results