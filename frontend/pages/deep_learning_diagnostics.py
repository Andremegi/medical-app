import streamlit as st
import pandas as pd
import requests
from modules.nav import Navbar

def colors(array):
    array.sort()

    color=[]
    for desease in array:
        if desease == 'Cumulative probability for 23 other deseases':
            color.append('#FFF8DC')
        else :
            color.append('#FF7F50')
    return color

def main():
    Navbar()

    st.title("Symptom-Desease Chatbot")
    st.write("Please, describe your symtoms so I can predict your disease")

    txt = st.text_area(
        "Write your symptoms here",
        """""",
    )
    params = {"symptoms": txt}
    url_text = "https://backend-1041725143942.europe-west1.run.app/symptoms"

    if st.button("Predict"):
        if txt == '' or txt== ' ':
            st.error('##### ⚠️Please describe your symptoms above')

        if txt != ' ' and txt != '':
            st.success("##### I'm working on your diagnosis")

            response_text = requests.get(url_text, params).json()


            # st.write(f"Your deseais is {response_text['disease']} with a probability = {round(float(response_text['probability']), 2)} %." )


            st.markdown(
                "<h3 style='margin:1; padding:1'>It seems your desease could be:</h3>",
                unsafe_allow_html=True,
                    )

                #Separating the data to make our dataset
            probs = (round(float(response_text['probability']), 2), (100-round(float(response_text['probability']), 2)))
            diseases = [response_text['disease'] , 'Cumulative probability for 23 other deseases']
            text_df= pd.DataFrame([probs] , columns= diseases, index=[0])
            st.metric(' ',response_text['disease'], ' ')
            graph_colors=  colors(diseases)
            #print(graph_colors)
            st.markdown(
                "<h4 style='text-align: center; margin:0; padding:0.5'>Prediction Probabilities</h4>",
                unsafe_allow_html=True)
            st.bar_chart(text_df,y_label='Deseases', x_label='Probability (%)', horizontal=True, color=graph_colors)




    else:
        st.write("Please press the button so I can make a prediction.")

    st.markdown(
        "<h3 style='text-align:center; margin:0; padding:0'>Still have questions on you health status? Try out our Doctor chatbot ⬇️ <br /><br /></h3>",
        unsafe_allow_html=True,
            )

    col1,col2,col3 = st.columns(3)

    if col2.button("Doctor Chatbot", use_container_width=True):
        st.switch_page("pages/llm_doctor_chatbot.py")

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
