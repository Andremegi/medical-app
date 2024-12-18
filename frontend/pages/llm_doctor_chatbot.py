import streamlit as st
import requests
import os

from modules.nav import Navbar


def main():
    Navbar()
    with st.container(key='interface'):
    #with st.container(border=False):
        st.title("Hugging face Chatbot")
        st.write("Please, describe your symtoms so we can talk about your possible disease")

        if "chat_history_api" not in st.session_state:
            st.session_state.chat_history_api = ""

        if "chat_history_area" not in st.session_state:
            st.session_state.chat_history_area = ""

            # Function to call the API (assuming you are running it locally on a FastAPI server)
        def call_api(user_input, chat_history):
            response = requests.get(
                "https://backend-1041725143942.europe-west1.run.app/chat-bot",
                params={"user_input": user_input, "chat_history": chat_history},
            )
            return response.json()

        user_input = st.text_area("Write your symptoms here")

        button = st.button("Ask")

        # Display the markdown content
        markdown_container = st.empty()
        markdown_container.markdown(st.session_state.chat_history_area)

            # When the user clicks the 'Ask' button
        if button and user_input:
            # Append the user's input to the chat history and display it immediately
            st.session_state.chat_history_area += f"\n**YOU** : {user_input}\n"
            markdown_container.markdown(st.session_state.chat_history_area)

            # Call the API with the current user input and previous chat history
            result = call_api(user_input, st.session_state.chat_history_api)

            # Update state with the API response
            response, chat_history_api = result["response"], result["chat_history"]
            st.session_state.chat_history_api = chat_history_api

            # Append bot response to the chat history
            st.session_state.chat_history_area += f"\n**DOCTOR AI** : {response}\n"
            markdown_container.markdown(st.session_state.chat_history_area)


    st.markdown(
    f"""
    <style>
    .st-key-interface{{
        border-style: solid;
        border-color:  #4daab2;
        border-radius: 10px;
        width: 750px;
        height: 100px;
        padding: 20px;
        background-image: url('https://i.ibb.co/JHdYRmC/incroyable.jpg');
    }}
    .stButton > button {{
        background-color: #4daab2;
        color: white;
    }}
    .stButton > button:hover {{
        background-color: #FFFFFF; /* WHITE */
        color: #4daab2;
        border-style: solid;
        border-radius: 8px;
        border-color: #4daab2;


    }}

    </style>
    """,
        unsafe_allow_html=True,
    )
if __name__ == "__main__":
    main()
