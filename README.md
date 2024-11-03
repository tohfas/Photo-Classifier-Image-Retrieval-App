# Photo Classifier - An Artificially Intelligent Image Retrieval System

## Introduction
The objective of this project is to develop a photo classifier system using AI Vision models. The system processes a dataset of images, allowing users to provide textual prompts to retrieve relevant images. 

## Methodology
Several modifications were made to enhance the original CLIP model's performance:

1. **Image Fetching Optimization**: Improved the process of retrieving images based on textual prompts to increase efficiency.
2. **Enhanced Embedding Creation**: Adjusted the method for creating and using text embeddings from images to better match user prompts.
3. **Top-5 Image Selection**: Implemented a feature to select the top 5 images that best matched the user's prompt, ensuring both relevance and speed.

These modifications were designed to maintain the core strengths of the CLIP model while addressing its limitations in real-time applications.

## Results

- **Speed**: The model's processing time was significantly reduced, with results being generated quicklu, making it efficient for real-world use.
- **Outcome**: The modified CLIP model emerged as the most optimal solution among the prototypes tested.

## Example Outputs
- **Prompt**: `"Flowers in the garden"`  
  **Result**: Retrieved the most Flowers in the garden images.

- **Prompt**: `"people with mask on face"`  
  **Result**: Provided images that accurately depicted people with mask on face.

## Conclusion
The modified CLIP model successfully met the project's objectives by providing a fast and accurate photo classification system. Its ability to process large datasets and retrieve relevant images based on textual prompts in near real-time makes it a viable solution for practical applications.

## Installation Instructions for Image Retriever

1. **Create a new Conda environment:**
```bash
   conda create --name Image_Retriever python=3.9
   ```

2. **Activate the environment:**
```bash
   conda activate Image_Retriever 
   ```

3. **Install required packages:**
```bash 
conda install pandas
conda install matplotlib
conda install pillow
conda install tqdm
conda install requests
conda install -c conda-forge transformers
conda install pytorch=2.4.1 cpuonly -c pytorch
conda install matplotlib
```

4. **Install additional Python packages:**
```bash
pip install farm-haystack
pip install gradio
pip install fastapi
pip install uvicorn
pip install python-multipart
```

5. **Install Jinja2 and Jupyter:**
```bash
conda install -c conda-forge jinja2
conda install jupyter
```

6. **Open VS Code and clone the repository:**
```bash
git clone repo_link
```

7. **Choose the created environment as the environment with all the necessary packages.**

8. **After choosing environment and done with the setups, run embeddings_script.py first**

9. **Next, to launch the webapp, run the Streamlit app: In the terminal, type:**
```bash
streamlit run app.py
```

