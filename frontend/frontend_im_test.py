import requests
from image_data.apifile import transform, create_upload_file
from image_data.model import im_transformation
from PIL import Image
import streamlit as st

# Streamlit interface
st.title("Image Recognition with Streamlit")
st.write("Upload an image to classify it!")

# alouds to give a name to save the im
name = st.text_input('Enter the name', 'Name')
surname = st.text_input('Enter the surname', 'Surname')

# Image uploader
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Display the uploaded image

    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Making transformation
    im_trans = transform(image)
    st.image(im_trans)

     # Classify image
    st.write("To do Classifying...")
    #label_idx = classify_image(image)
    #st.write(f"Predicted label index: {label_idx}")


#Image saver

st.markdown("""
    ## ¿Would you like to **save** the original image ?
""")

save_image = st.button('Save image')

if save_image == True:
    name = f'{surname}_{name}'
    create_upload_file(image, name)
    st.write('Image has been saved ✅')

else :
    st.write("Your image isn't jet saved")
