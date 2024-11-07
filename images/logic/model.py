import os
import numpy as np
from keras.api.models import load_model
from keras.api.preprocessing.image import load_img, img_to_array

def load():
    # Load the saved model
    dir_path = os.path.dirname(__file__)
    model_path = os.path.join(dir_path, 'model_1.keras')
    model = load_model(model_path)

    return model

def predict(model, image_path):
    # Load and preprocess the image
    img = load_img(image_path, target_size=(150, 150))  # Resize to match model input
    img_array = img_to_array(img)  # Convert to array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict class
    predictions = model.predict(img_array)

    # Identify the index of the highest probability
    class_idx = np.argmax(predictions, axis=1)[0]

    # Define class labels
    class_labels = ['Normal', 'Lung Opacity', 'Viral Pneumonia']

    # Map each class to its prediction probability
    predictions_per_label = {class_labels[i]: float(predictions[0][i]) for i in range(len(class_labels))}

    # Get the best label
    best_label = class_labels[class_idx]

    return best_label, predictions_per_label
