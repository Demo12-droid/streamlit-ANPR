import streamlit as st
from PIL import Image

st.title("ANPR")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image on the left
    col1, col2 = st.columns(2)
    
    with col1:
        uploaded_image = Image.open(uploaded_file)
        st.image(uploaded_image, caption='Uploaded Image', use_column_width=True)
    
    # Placeholder for the second image (you can replace this with your own image path)
    second_image = uploaded_file
    
    # Display the second image on the right
    with col2:
        st.image(second_image, caption='Annotated Image', use_column_width=True)

st.subheader("Number Plates Data")

# Create a DataFrame to store the data
df_data = {
    "Class": [class_value],
    "Number Plate": [number_plate]
}

df = pd.DataFrame(df_data)

# Display the dataframe
st.subheader("Number Plates Data:")
st.write(df)
