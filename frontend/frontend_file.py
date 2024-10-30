import requests
import streamlit as st

# Page title
st.set_page_config(page_title="Lung Cancer Questionnaire")
st.title("Lung Cancer Questionnaire")

# User input fields
with st.form(key="questionnaire_form"):
    # Sex
    sex = st.radio("Sex", options=["Male", "Female"])

    # Smoking
    smoking = st.radio("Do you smoke?", options=["Yes", "No"])

    # Yellow fingers
    yellow_fingers = st.radio("Do you have yellow fingers?", options=["Yes", "No"])

    # Anxiety
    anxiety = st.radio("Do you have anxiety?", options=["Yes", "No"])

    # Peer pressure
    peer_pressure = st.radio("Do you have peer pressure?", options=["Yes", "No"])

    # Chronic disease
    chronic_disease = st.radio("Do you have chronic disease?", options=["Yes", "No"])

    # Fatigue
    fatigue = st.radio("Do you have fatigue?", options=["Yes", "No"])

    # Allergy
    allergy = st.radio("Do you have allergy?", options=["Yes", "No"])

    # Wheezing
    wheezing = st.radio("Do you have wheezing?", options=["Yes", "No"])

    # Alcohol consumption
    alcohol_consumption = st.radio("Do you consume alcohol?", options=["Yes", "No"])

    # Coughing
    coughing = st.radio("Do you have a cough?", options=["Yes", "No"])

    # Shortness of breath
    shortness_of_breath = st.radio("Do you have shortness of breath?", options=["Yes", "No"])

    # Swallowing difficulties
    swallowing_difficulties = st.radio("Do you have swallowing difficulties?", options=["Yes", "No"])

    # Chest pain
    chest_pain = st.radio("Do you have chest pain?", options=["Yes", "No"])

    # Age
    age = st.number_input("Age", min_value=0, step=1)

    # Submit button
    submitted = st.form_submit_button(label="Submit")

url = 'https://tabular-data-1041725143942.europe-west1.run.app/predict'

if submitted:
    # Store the results in a dictionary
    params = {
        "gender": "M" if sex == "Male" else "F",
        "smoking": 2 if smoking == "Yes" else 1,
        "yellow_fingers": 2 if yellow_fingers == "Yes" else 1,
        "anxiety": 2 if anxiety == "Yes" else 1,
        "peer_pressure": 2 if peer_pressure == "Yes" else 1,
        "chronic_disease": 2 if chronic_disease == "Yes" else 1,
        "fatigue": 2 if fatigue == "Yes" else 1,
        "allergy": 2 if allergy == "Yes" else 1,
        "wheezing": 2 if wheezing == "Yes" else 1,
        "alcoholl": 2 if alcohol_consumption == "Yes" else 1,
        "coughing": 2 if coughing == "Yes" else 1,
        "shortness_breath": 2 if shortness_of_breath == "Yes" else 1,
        "swalloging_difficulty": 2 if swallowing_difficulties == "Yes" else 1,
        "chest_pain": 2 if chest_pain == "Yes" else 1,
        "age": age
    }

    response = requests.get(url, params=params)
    prediction = response.json()

    st.write("Questionnaire Results:")
    st.write(prediction)
