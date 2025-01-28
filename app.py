# Description: This file is the main file for the streamlit app. It is used to run the streamlit app.
from dotenv import load_dotenv
import streamlit as st

import chain

load_dotenv()

def poem_generation_app():
    # This function creates a simple Streamlit app for generating poems based on a user-provided topic.
    # It contains the following steps:
    # 1. A form is created using Streamlit's `st.form` method with the identifier "poem_generating_form".
    # 2. Inside the form, a text input field is added for the user to specify the topic of the poem.
    # 3. A submit button is included in the form, which, when clicked, triggers the form submission.
    # 4. On form submission, the `generate_poem` method from the `chain` object is called with the provided topic.
    # 5. The response, which is the generated poem, is displayed in the app using Streamlit's `st.write` function.
    with st.form("poem_generater"):
        topic=st.text_input("enter the topic")
        submitted=st.form_submit_button("generate")
        if(submitted):
            # topic+=" - generate 8 line poem from the above"
            response = chain.poem(topic)
            st.info(response)

poem_generation_app()