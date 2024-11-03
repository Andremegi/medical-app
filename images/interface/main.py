import os

from images.logic.model import load, predict


if __name__ == "__main__":
    model = load()

    # Define the path for the test image
    dir_path = os.path.dirname(__file__)
    test_image_path = os.path.join(dir_path, 'test_lung_opacity.jpg')  # Make sure the image is current directory

    if os.path.exists(test_image_path):
        label, probability = predict(model, test_image_path)
        print(f"Predicted label: {label}")
        print(f"Predicted probabilities: {probability}")
    else:
        print("Test image not found. Please ensure 'test.img' is in the root directory.")
