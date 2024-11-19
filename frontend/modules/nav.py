import streamlit as st


def Navbar():
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Homepage', icon='🫁')
        st.page_link('pages/images_analysis.py', label='Image Analysis', icon='🩻')
        st.page_link('pages/chatbot.py', label='Chatbot', icon='👨🏻‍⚕️')

