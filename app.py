import streamlit as st
from multimodal_image_search import MultimodalSearch

# Set the layout configuration for the Streamlit page
st.set_page_config(layout="wide")

# Custom CSS for styling the app's title, background, and button
st.markdown("""<style>
    .stApp {
        background-color: #f0f0f0;
    }
    h1 {
        color: blue;
        text-align: center;
    }
    div.stButton > button {
        background-color: blue;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #0056b3;
    }
</style>""", unsafe_allow_html=True)

def main():
    # Display the title of the app in the center of the page
    st.markdown("<h1>Photo Classifier Image Retrieval App</h1>", unsafe_allow_html=True)
    
    # Initialise the MultimodalSearch class which handles text-to-image retrieval
    multimodal_image_search = MultimodalSearch()

    # Create a text input widget for the user to enter their search query
    prompt = st.text_input("Enter your prompt to search images:")

    # Create a button that triggers the search when clicked
    if st.button("Search"):
        # Check if the user has entered a valid prompt
        if len(prompt) > 0:
            results = multimodal_image_search.search_images(prompt)
            st.warning("Your query was: " + prompt)
            st.subheader("Search Results:")

            if results:
                # Limit to a maximum of 5 images
                results_to_display = results[:5]
                
                # Create columns to display the images side by side
                cols = st.columns(len(results_to_display))  # Create as many columns as there are results
                for col, result in zip(cols, results_to_display):

                    col.image(result.content, use_column_width=True)
            else:
                st.error("No results found.")  # Show error if no results
            
        else:
            st.warning("Please enter your prompt to search images.")  # Warn if no prompt is entered

# Ensure that the app runs when the script is executed
if __name__ == "__main__":
    main()
