import streamlit as st
from multimodal_image_search import MultimodalSearch
from PIL import Image
import io
import os
import base64

# Set the layout configuration for the Streamlit page
st.set_page_config(layout="wide")

# Custom CSS for styling the app's title, background, and buttons
st.markdown("""
<style>
.stApp {
    background-color: #f0f0f0;
}
h1 {
    color: #003366;
    text-align: center;
    font-family: 'Arial', sans-serif;
    padding: 10px;
    margin-bottom: 20px;
}
.image-container {
    position: relative;
    width: 100%;
    display: inline-block;
}
.image-container img {
    width: 100%;
    height: auto;
    border-radius: 10px;
}
.download-button {
    position: absolute;
    top: 10px;
    left: 10px;
    background-color: rgba(255, 255, 255, 0.8);
    border: none;
    border-radius: 50%;
    padding: 10px;
    cursor: pointer;
    box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
}
.download-button:hover {
    background-color: rgba(255, 255, 255, 1);
}
</style>
""", unsafe_allow_html=True)

# Function to load and convert the image to bytes for download
def get_image_bytes(image_path):
    img = Image.open(image_path)
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="JPEG")
    img_bytes.seek(0)  # Rewinding the file-like object to the beginning
    return img_bytes

# Function to convert image bytes to base64 for displaying in HTML
def image_to_base64(image_bytes):
    return base64.b64encode(image_bytes.getvalue()).decode()

def main():
    # Displaying the title of the app in the center of the page
    st.markdown("<h1>Photo Classifier Image Retrieval App</h1>", unsafe_allow_html=True)

    # Initialising the MultimodalSearch class which handles text-to-image retrieval
    multimodal_image_search = MultimodalSearch()

    # Creatinge a text input widget for the user to enter their search query
    prompt = st.text_input("Enter your prompt to search images:")

    # Creating a button that triggers the search when clicked
    if st.button("Search"):
        # Checking if the user has entered a valid prompt
        if len(prompt) > 0:
            results = multimodal_image_search.search_images(prompt)
            st.warning("Your query was: " + prompt)
            st.subheader("Search Results:")

            if results:  # Check if results are found
                # Limiting to a maximum of 5 images
                results_to_display = results[:5]

                # Creating columns to display the images side by side
                cols = st.columns(len(results_to_display))

                # Creating as many columns as there are results
                for i, result in enumerate(results_to_display):
                    with cols[i]:
                        # Aligning image and button in the same column
                        # Getting image bytes for download and display image
                        image_bytes = get_image_bytes(result.content)
                        base64_image = image_to_base64(image_bytes)

                        # Displaying the image with download button overlaid
                        st.markdown(f"""
                        <div class="image-container">
                            <img src="data:image/jpeg;base64,{base64_image}" alt="Image {i+1}">
                            <a href="data:image/jpeg;base64,{base64_image}" download="{os.path.basename(result.content)}" class="download-button" title="Download"> ⬇ </a>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.error("No results found.")  # Showing error if no results found
        else:
            st.warning("Please enter your prompt to search images.")  # Warning if no prompt is entered

# Ensuring that the app runs when the script is executed
if __name__ == "__main__":
    main()
