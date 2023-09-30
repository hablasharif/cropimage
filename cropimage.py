import streamlit as st
from PIL import Image, ImageDraw
import io
import base64

# Streamlit app title
st.title("Advanced Image Cropper")

# User input for uploading an image file
uploaded_image = st.file_uploader("Upload an image file:", type=["jpg", "jpeg", "png", "gif"])

# Function to crop the image
def crop_image(image, x, y, width, height):
    try:
        img = Image.open(image)
        cropped_img = img.crop((x, y, x + width, y + height))
        return cropped_img
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# Display the cropped image
if uploaded_image:
    st.subheader("Original Image:")
    st.image(uploaded_image, use_column_width=True)
    
    st.subheader("Image Cropping:")
    x = st.number_input("X (pixels):", step=1)
    y = st.number_input("Y (pixels):", step=1)
    width = st.number_input("Width (pixels):", step=1)
    height = st.number_input("Height (pixels):", step=1)
    
    if st.button("Crop Image"):
        cropped_img = crop_image(uploaded_image, x, y, width, height)
        if cropped_img:
            st.subheader("Cropped Image:")
            st.image(cropped_img, use_column_width=True)

            # Option to download the cropped image
            st.markdown(get_binary_file_downloader_html(cropped_img, "cropped"), unsafe_allow_html=True)

# Function to create a download link for the image
def get_binary_file_downloader_html(image, file_label):
    img_byte_array = io.BytesIO()
    image.save(img_byte_array, format="PNG")
    b64 = base64.b64encode(img_byte_array.getvalue()).decode()
    href = f'<a href="data:image/png;base64,{b64}" download="{file_label}.png">Download {file_label}</a>'
    return href
