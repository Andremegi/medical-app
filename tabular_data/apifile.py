from fastapi import FastAPI
import pickle
from tabular_data.model import prediction_tabular_data

app = FastAPI()

@app.get('/')
def root():
    return {'medical-app says': 'Hello team'}


@app.get("/predict")
def predict(gender,age, smoking,yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcoholl, coughing, shortness_breath,swalloging_difficulty, chest_pain):
    #Get the prediction with the information that we provide
    response = prediction_tabular_data(gender,age, smoking,yellow_fingers, anxiety, peer_pressure, chronic_disease, fatigue, allergy, wheezing, alcoholl, coughing, shortness_breath,swalloging_difficulty, chest_pain)[0]
    if response == 1:
        response_translated = 'You have lung cancer '
    if response == 0:
        response_translated = "You don't have lung cancer"
    return {'The prediction is that ': response_translated}
