import streamlit as st
import pandas as pd
import requests
from modules.nav import Navbar


def main():
    Navbar()

    st.title("Symptom-Desease Chatbot")
    st.write("Please, describe your symtoms so I can predict your disease")

    txt = st.text_area(
        "Write your symptoms here",
        """

        """,
    )
    params = {"symptoms": txt}
    url_text = "https://backend-1041725143942.europe-west1.run.app/symptoms"

    if st.button("Predict"):

        response_text = requests.get(url_text, params).json()
        st.write(
            f"Your deseais is {response_text['disease']} with a probability = {round(float(response_text['probability']), 2)} %."
        )
        st.markdown(
        "<h3 style='margin:1; padding:1'>Your desease is:</h3>",
        unsafe_allow_html=True,
            )

        probs = (round(float(response_text['probability']), 2), (100-round(float(response_text['probability']), 2)))
        diseases = [response_text['disease'] , 'Other diseases']
        text_df= pd.DataFrame([probs] , columns= diseases, index=[0])
        st.metric(' ',response_text['disease'], ' ')

        st.bar_chart(text_df)

    else:
        st.write("Please press the button so I can make a prediction.")


    st.markdown(
        """
    <style>
    .stMetric {
        font-weight: bold;
        text-align: center;
        background-color: #D3D3D3;
        margin: auto;

        width : auto;

    }
    .stButton > button {
        background-color: #4daab2;
        color: white;
    }
    .stButton > button:hover {
        background-color: #FFFFFF; /* WHITE */
        color: #4daab2;
        border-style: solid;
        border-radius: 8px;
        border-color: #4daab2;


    }
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
