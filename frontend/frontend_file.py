import requests
import streamlit as st
from PIL import Image
import torch
from torchvision import models, transforms

# Load a pre-trained model (e.g., ResNet)
model = models.resnet50(pretrained=True)
model.eval()

# Define transformation to preprocess the uploaded image
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
# Define a function for image classification
def classify_image(image):
    # Preprocess the image
    image = preprocess(image).unsqueeze(0)
    # Get prediction
    with torch.no_grad():
        output = model(image)
    # Get the label
    _, predicted_idx = torch.max(output, 1)
    return predicted_idx.item()

# Streamlit interface
st.title("Image Recognition with Streamlit")
st.write("Upload an image to classify it!")

# Image uploader
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Prepare the image for sending to the API
    # The uploaded_file is already in bytes-like format
    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}

    # Send the image to the API
    response = requests.post("http://127.0.0.1:8000/upload-image/", files=files)

    if response.status_code == 200:
        # Process the response from the API
        result = response.json()
        st.write("Image saved successfully!")
        st.write(f"Filename: {result['filename']}")
        st.write(f"Saved path: {result['path']}")
    else:
        st.write("Failed to upload the image to the API.")
