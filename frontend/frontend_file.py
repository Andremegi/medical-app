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

if submitted:
    # Store the results in a dictionary
    questionnaire_results = {
        "sex": sex == "Male",
        "smoking": smoking == "Yes",
        "yellow_fingers": yellow_fingers == "Yes",
        "anxiety": anxiety == "Yes",
        "alcohol_consumption": alcohol_consumption == "Yes",
        "coughing": coughing == "Yes",
        "shortness_of_breath": shortness_of_breath == "Yes",
        "swallowing_difficulties": swallowing_difficulties == "Yes",
        "chest_pain": chest_pain == "Yes",
        "age": age
    }

    st.write("Questionnaire Results:")
    st.write(questionnaire_results)
