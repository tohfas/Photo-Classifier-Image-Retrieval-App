import streamlit as st
from multimodal_search import MultimodalSearch

st.set_page_config(
    layout="wide"
)

def main():
    st.markdown("<h1 style='text-align: center; color: green;'>Photo Classifier Image Retrieval App</h1>", unsafe_allow_html=True)
    data_file = "tmp/photos.tsv000"
    multimodal_search = MultimodalSearch(data_file)

    prompt = st.text_input("Enter your query:")
    if st.button("Search"):
        if len(prompt) > 0:
            results = multimodal_search.search_images(prompt, top_k=5)
            st.warning("Your query was "+prompt)
            st.subheader("Search Results:")
            col1, col2, col3, col4, col5 = st.columns([1,1,1,1,1])
            with col1:
                st.image(results[0][0], use_column_width=True)
            with col2:
                st.image(results[1][0], use_column_width=True)
            with col3:
                st.image(results[2][0], use_column_width=True)
            with col4:
                st.image(results[3][0], use_column_width=True)
            with col5:
                st.image(results[4][0], use_column_width=True)
        else:
            st.warning("Please enter a query.")

if __name__ == "__main__":
    main()