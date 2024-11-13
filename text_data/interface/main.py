import os

from text_data.model import load_model, predict


if __name__ == "__main__":
    phrase =['It burns when i urinate']


    label, probability = predict(phrase)
    print(f"Predicted label: {label}")
    print(f"Predicted probabilities: {probability}")
