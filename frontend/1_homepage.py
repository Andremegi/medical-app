import streamlit as st
import os


st.set_page_config(page_title="Homepage for Medical-app")
st.image("docs/logo.png")

st.markdown(
    "<h2 style='text-align: center;'>BREATHE AGAIN 🌬️</h2>", unsafe_allow_html=True
)

st.markdown(
    "<h1 style='text-align: center; margin:0; padding:0'></h1>", unsafe_allow_html=True
)


st.markdown(
    "<h1 style='text-align: center; margin:0; padding: 0'>Welcome to COMPALUNG, </h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<h2 style='text-align: center;; padding: 0'>Your companion for respiratory health</h2>",
    unsafe_allow_html=True,
)

st.sidebar.success("Select a page")

st.markdown(
    "<h1 style='text-align: center; margin:0; padding:0'></h1>", unsafe_allow_html=True
)


# Custom CSS to style and center the button
st.markdown(
    """
    <style>
    .stButton > button {
        margin: auto; /* Center horizontally */
        display: block;
        background-color: #28a745; /* Success Green */
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #218838; /* Darker Green */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create columns to center the button
# col1, col2, col3 = st.columns([1, 2, 2]) # Center button in the middle column

# with col2:
if st.button("Start analysis"):
    st.switch_page("pages/2_☢️Images_analysis.py")  # Switch to the target page
