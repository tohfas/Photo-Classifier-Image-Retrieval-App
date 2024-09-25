import streamlit as st
from multimodal_image_search import MultimodalSearch

# Set the layout configuration for the Streamlit page
st.set_page_config(layout="wide")

# Custom CSS for styling the app's title, background, and button
st.markdown("""
    <style>
    /* Change background to grey */
    .stApp {
        background-color: #f0f0f0;
    }

    /* Style the title */
    h1 {
        color: blue;
        text-align: center;
    }

    /* Style the button */
    div.stButton > button {
        background-color: blue;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
        border: none;
    }

    /* Button hover effect */
    div.stButton > button:hover {
        background-color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True)


def main():

    # Display the title of the app in the center of the page, with green color
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
            st.warning("Your query was "+prompt)
            st.subheader("Search Results:")

            # Create five columns to display the top 5 images side by side
            column1, column2, column3, column4, column5 = st.columns([1,1,1,1,1])

            with column1:
                
                st.image(results[0].content, use_column_width=True)

            with column2:
                
                st.image(results[1].content, use_column_width=True)

            with column3:
                
                st.image(results[2].content, use_column_width=True)

            with column4:
                
                st.image(results[3].content, use_column_width=True)

            with column5:
                
                st.image(results[4].content, use_column_width=True)
        else:
            # If the user hasn't entered any prompt, display a warning message
            st.warning("Please enter a your prompt to search images.")

# Ensure that the app runs when the script is executed
if __name__ == "__main__":
    main()