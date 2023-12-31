#!/usr/bin/env python
# coding: utf-8

## Importing the libraries required for streamlit
## Important note, is that if you want to upload more packages, you need to update the requirements file and re-upload it to Streamlit

import os ## For file management
import streamlit as st ## Streamlit library for creating the web app
from PIL import Image ## Image library for displaying images
from streamlit_option_menu import option_menu ## What should be displayed on the side bar? 
# from streamlit_oauth import OAuth2Component ## For login credentials for potential follow up pages?

## Creating a side bar for the user
with st.sidebar:
    selected = option_menu("Kidney Stone Prediction App", ["Home", 'Kidney Stone Predictor', 'Next Steps'], 
        icons=['house-door-fill', 'hospital-fill', 'emoji-smile-fill'], menu_icon="cast", default_index=1)
    selected
    
st.write("This project was prepared fro Prof Teo # Placeholder text ")
image = Image.open('pneumonia inception v3.jpeg')
st.image(image, caption='Placeholder image',use_column_width=True)


st.subheader('Please enter the relevant details below')

def get_user_input():
    gravity = st.number_input("Please enter the gravity here: 👇")
    ph = st.number_input("Please enter the PH level here: 👇")
    osmo = st.number_input("Please enter the osmo here: 👇")
    cond = st.number_input("Please enter the condition here: 👇")
    urea = st.number_input("Please enter the urea here: 👇")
    calc = st.number_input("Please enter the calc here: 👇")
    ## Prediction here is manually coded as can be seen in the original file provided 
    prediction = -0.04191465 + (gravity * -3.94579654e-02) + (ph * -3.94579654e-02) + (osmo * 3.05883681e-04) + (cond * -8.53476004e-02) + (urea * 1.12604054e-03) + (calc * 7.20512124e-01)
    return round(prediction, 5)

prediction = get_user_input() ## Getting user input

st.subheader('Press the button below to submit your information and get results: ')
if st.button('Submit information!'): ## If button pressed, result will be shown. Else nothing will be shown. 
    st.subheader("These are your results: ")
    st.write(prediction)





