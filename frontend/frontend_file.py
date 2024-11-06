import requests
import streamlit as st
from PIL import Image

# Streamlit interface
st.title("Image Recognition with Streamlit")
st.write("Upload an image to classify it!")

# Image uploader
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert the uploaded file to bytes for the API request
    uploaded_file.seek(0)  # Reset the file pointer to the beginning
    file_bytes = uploaded_file.read()  # Read file content as bytes

    # Prepare the file for sending
    files = {
        "file": (uploaded_file.name, file_bytes, uploaded_file.type)
    }

    # Send the image to the API
    response = requests.post("https://backend-1041725143942.europe-west1.run.app/upload-image/", files=files)

    if response.status_code == 200:
        # Process the response from the API
        result = response.json()
        st.write("Image processed and predicted !")
        st.write(f"Predicted class: {result['label']}")
    else:
        st.write("Failed to upload the image to the API.")
