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

     # Classify image
    st.write("Classifying...")
    label_idx = classify_image(image)
    st.write(f"Predicted label index: {label_idx}")
