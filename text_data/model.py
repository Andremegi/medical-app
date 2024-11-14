import os
import numpy as np
from tensorflow.keras.preprocessing.text import  Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.api.models import load_model
import pickle

def preprocessing(symptoms):
    '''
    Preprocess the sypmtoms, tokenizing and padding the sequence that
    the user passes
    '''
    dir_path = os.path.dirname(__file__)
    tokienizer_path = os.path.join(dir_path,'models', 'tokenizer.pickle')

    with open(tokienizer_path, 'rb') as handle:
        tk = pickle.load(handle)

    symptoms_tokenized = tk.texts_to_sequences(symptoms) #tokenization of the symptoms that users introduce
    symptoms_padded = pad_sequences(symptoms_tokenized, padding='pre') # forward padding of the tokenized sequence

    return symptoms_padded


def load():
    '''
    Loads the saved model
    '''
    # Load the saved model
    dir_path = os.path.dirname(__file__)
    model_path = os.path.join(dir_path,'models', 'model_nll_84.keras')
    model = load_model(model_path)

    return model

def predict(symptoms):
    '''
    Predict what is the desease that seems that correspond with the
    given symptoms
    '''

    diseases = ['Acne','Arthritis','Bronchial Asthma','Cervical spondylosis',
 'Chicken po','Common Cold','Dengue','Dimorphic Hemorrhoids','Fungal infection',
 'Hypertension','Impetigo','Jaundice','Malaria','Migraine','Pneumonia','Psoriasis',
 'Typhoid','Varicose Veins','allergy','diabetes','drug reaction',
 'gastroesophageal reflux disease','peptic ulcer disease','urinary tract infection']

    # preprocess symptoms
    preprocessed_symptoms = preprocessing(symptoms)

    #load the model
    model = load()

    # make the prediction
    prediction = model.predict(preprocessed_symptoms)

    # get the index of the max probability
    max_prob = np.argmax(prediction)

    #look for the index in our deseases
    disease = diseases[max_prob]
    return disease, max_prob
