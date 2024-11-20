import streamlit as st
import requests
from PIL import Image
import pandas as pd
from modules.nav import Navbar

colors=['#FF8C00', '#006400', '#8B0000' ]


def main():
    Navbar()

    st.title("Lung X-Ray Image Analysis")
    st.write("Please upload an image of the **X-Ray** you want to analyze.")

    # Image uploader
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Convert the uploaded file to bytes for the API request
        uploaded_file.seek(0)  # Reset the file pointer to the beginning
        file_bytes = uploaded_file.read()  # Read file content as bytes

        # Prepare the file for sending
        files = {"file": (uploaded_file.name, file_bytes, uploaded_file.type)}

        # Send the image to the API
        url = 'https://backend-1041725143942.europe-west1.run.app/upload-image/'

        response = requests.post(url, files=files)

        if response.status_code == 200:
            # Process the response from the API
            result = response.json()

            st.success("###### Your image has been processed and predicted")
            st.markdown(
        "<h3 style='margin:1; padding:1'>Your lung condition looks like :</h3>",
        unsafe_allow_html=True,
            )


            st.metric('', result['best_label'])
            st.markdown(
        "<h1 style='text-align: center; margin:0; padding:0'></h1>",
        unsafe_allow_html=True,
            )


            predictions_per_label = result["predictions_per_label"]
            st.write("##### Prediction Probabilities")
            for label, probability in predictions_per_label.items():
                st.write(f"{label}: {probability * 100:.2f}%")

            predictions_per_label_df = pd.DataFrame(predictions_per_label, index=[0])
            print(predictions_per_label_df)
            st.bar_chart(predictions_per_label_df,
                         x_label = 'Diseases',
                         y_label ='Probability',
                         horizontal=False,
                         stack=False,
                         color = colors)


        else:
            st.error("Failed to upload the image to the API.")

    st.write("##### Would you like to have a deeper analysis on your health status?")
    st.write(
        "If yes please , select the button bellow or go to the page 'Chatbot' on the left size"
    )
    if st.button("Deeper analysis"):
        st.switch_page("pages/3_💬Chatbot.py")  # need to update to 1.40.0
    else:
        st.write("Button has not been jet pressed")

    st.markdown(
        """
    <style>
    .stMetric {
        font-weight: bold;
        text-align: center;
        background-color: #D3D3D3;

    }

    }
    </style>
    """,
        unsafe_allow_html=True,
    )
if __name__ == "__main__":
    main()
