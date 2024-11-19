import os
import numpy as np
from keras.api.models import load_model
from keras.api.preprocessing.image import load_img, img_to_array
from google.cloud import storage
from images.params import *
from tensorflow import keras

def load():
    if MODEL_TARGET == "GCS":
        return load_model_from_gcs_or_local()

    return load_local()

def load_local():
    # Load the saved model
    dir_path = os.path.dirname(__file__)
    model_path = os.path.join(dir_path, 'model_1.keras')
    model = load_model(model_path)

    return model

def load_model_from_gcs_or_local():
    model_name = 'model_3.keras'
    local_model_path = os.path.join(LOCAL_MODEL_PATH, model_name)

    # Check if the model exists locally
    if os.path.exists(local_model_path):
        print(f"✅ Model found locally at {local_model_path}")
        try:
            model = keras.models.load_model(local_model_path)
            print("✅ Model loaded successfully from local storage")
            return model
        except Exception as e:
            print(f"❌ Error loading model locally: {str(e)}")
            return None

    print("❌ Model not found locally. Fetching from GCS...")

    # Load model from GCS
    try:
        client = storage.Client()
        blobs = list(client.get_bucket(BUCKET_NAME).list_blobs(prefix="images/"))

        # Find the specific model
        model_blob = next((blob for blob in blobs if blob.name.endswith(model_name)), None)
        if not model_blob:
            print(f"❌ Model '{model_name}' not found in GCS under 'images/'")
            return None

        # Download the model
        os.makedirs(LOCAL_MODEL_PATH, exist_ok=True)
        model_blob.download_to_filename(local_model_path)
        print(f"✅ Model downloaded from GCS to {local_model_path}")

        # Load the model
        model = keras.models.load_model(local_model_path)
        print("✅ Model loaded successfully from GCS")
        return model
    except Exception as e:
        print(f"❌ Error loading model from GCS: {str(e)}")
        return None

# Only use it to save the big model from your computer to Google cloud
def save_model_gcs(model_full_path):
    model_filename = model_full_path.split("/")[-1]
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(f"images/{model_filename}")
    blob.upload_from_filename(model_full_path)
    print("✅ Model saved to GCS")

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
