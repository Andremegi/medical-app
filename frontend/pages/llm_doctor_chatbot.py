import streamlit as st
import requests

from modules.nav import Navbar


def main():
    Navbar()

    st.title("Hugging face Chatbot [beta]")
    st.write("Please, describe your symtoms so I can predict your disease")

    chat_history = ""

    # Function to call the API (assuming you are running it locally on a FastAPI server)
    def call_api(user_input, chat_history):
        response = requests.get(
            'https://backend-1041725143942.europe-west1.run.app/chat-bot',
            params={"user_input": user_input, "chat_history": chat_history},
        )
        return response.json()

    user_input = st.text_area(
        "Write your symptoms here",
        """

        """,
    )
    # When the user clicks the 'Ask' button
    if st.button("Ask"):
        if user_input:
            # Call the API with the current user input and the previous chat history
            result = call_api(user_input, chat_history)

            # Display the user input and the bot's response
            chat_history += result["chat_history"]

            # Show the updated chat history
            #st.text_area("Chat History", value=chat_history, height=300)
            st.text_area("Updated Chat History", value=chat_history, height=300)

    # Display the current chat history (user's messages and bot's responses)
    st.text_area("Chat History", value=chat_history, height=300, disabled=True)


if __name__ == "__main__":
    main()
