import numpy as np
from keras.api.models import load_model
from keras.api.preprocessing.image import load_img, img_to_array

def load_model_and_predict(image_path, model_path="model_1.keras"):
    # Load the saved model
    model = load_model(model_path)

    # Load and preprocess the image
    img = load_img(image_path, target_size=(150, 150))  # Resize to match model input
    img_array = img_to_array(img)  # Convert to array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict class
    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions, axis=1)[0]
    class_labels = ['Normal', 'Lung_Opacity', 'Viral Pneumonia']  # Update as per your model classes

    return class_labels[class_idx], predictions
