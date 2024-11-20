import streamlit as st
import requests
from modules.nav import Navbar


def main():
    Navbar()

    st.title("Generic medical Chatbot")
    st.write("Please, describe your symtoms so I can predict your disease")

    txt = st.text_area(
        "Write your symptoms here",
        """

        """,
    )
    params = {"symptoms": txt}
    url_text = "https://backend-1041725143942.europe-west1.run.app/symptoms"

    if st.button("Predict"):

        # print is visible in the server output, not in the page
        print(type(txt))
        st.write(txt)
        st.write("Predicting your desease...")
        response_text = requests.get(url_text, params).json()
        st.write(
            f"Your deseais is {response_text['disease']} with a probability = {round(float(response_text['probability']), 2)} %."
        )
    else:
        st.write("Please press the button so I can make a prediction.")


if __name__ == "__main__":
    main()
