import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel
import pandas as pd

# Load the CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Load your dataset
df = pd.read_csv('image_descriptions2.csv')  # Replace with your actual CSV file path


image_paths = df['image_file'].tolist()
descriptions = df['description'].tolist()

# Preprocess the images and descriptions
images = [Image.open(image_path).convert("RGB") for image_path in image_paths]
inputs = processor(text=descriptions, images=images, return_tensors="pt", padding=True)

# Compute the embeddings
outputs = model(**inputs)
image_features = outputs.image_embeds
text_features = outputs.text_embeds

# Function to search for relevant images given a prompt
def search_images(prompt, image_paths, text_features, top_k=5):
    # Preprocess the prompt
    inputs = processor(text=[prompt], return_tensors="pt", padding=True)
    prompt_features = model.get_text_features(**inputs)
    
    # Compute cosine similarity between the prompt and image descriptions
    similarities = torch.nn.functional.cosine_similarity(prompt_features, text_features)
    
    # Get the top k most similar images
    top_k_indices = similarities.topk(k=top_k).indices
    
    return [(image_paths[idx], similarities[idx].item()) for idx in top_k_indices]

# Main interactive loop
if __name__ == "_main_":
    prompt = input("Enter your search prompt: ")  # Let the user input the prompt
    top_k = int(input("Enter the number of top results you want: "))
    
    results = search_images(prompt, image_paths, text_features, top_k=top_k)
    
    print("\nTop relevant images based on your prompt:")
    for image_path, score in results:
        print(f"Image: {image_path}, Similarity Score: {score}")