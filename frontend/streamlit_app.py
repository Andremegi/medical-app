import streamlit as st
import os
from modules.nav import Navbar


def main():
    Navbar()

    st.title(f"Homepage for Medical-app")

    dir_path = os.path.dirname(__file__)
    image_folder_path = os.path.join(dir_path, "docs", "logo.png")
    st.image(image_folder_path)

    st.markdown(
        "<h2 style='text-align: center;'>BREATHE AGAIN 🌬️</h2>", unsafe_allow_html=True
    )

    st.markdown(
        "<h1 style='text-align: center; margin:0; padding:0'></h1>",
        unsafe_allow_html=True,
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
        "<h1 style='text-align: center; margin:0; padding:0'></h1>",
        unsafe_allow_html=True,
    )

    # Custom CSS to style and center the button
    st.markdown(
        """
    <style>
    .stImage {
        justify-content: center;
        text-align: center;
        display: block;
        margin-left: 100;
        margin-right: 100;
    }
    .stButton > button {
        margin: auto; /* Center horizontally */
        display: block;
        background-color: #4daab2; /* Success Green */
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
    }
    .stButton > button:hover {
        background-color: #FFFFFF; /* WHITE */
        color: #4daab2; /* Success Green */
        border-style: solid;
        border-radius: 8px;
        border-color: #4daab2;


    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    if st.button("Start analysis"):
        st.switch_page("pages/2_☢️Images_analysis.py")  # Switch to the target page


if __name__ == "__main__":
    main()
