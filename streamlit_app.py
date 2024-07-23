import streamlit as st
from PIL import Image

st.title("ANPR")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    image=st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

    # Placeholder for the second image (you can replace this with your own image path)
    second_image = image

    # Display the second image
    st.image(second_image, caption='Second Image', use_column_width=True)

