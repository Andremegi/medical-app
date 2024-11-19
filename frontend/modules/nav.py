import streamlit as st


def Navbar():
    with st.sidebar:
        st.page_link('streamlit_app.py', label='Homepage', icon='🫁')
        st.page_link('pages/images_analysis.py', label='X-Ray Analysis', icon='🩻')
        st.page_link('pages/deep_learning_diagnostics.py', label='Deep Diagnostics', icon='🩺')
        st.page_link('pages/llm_doctor_chatbot.py', label='LLM Doctor', icon='👨🏻‍⚕️')

