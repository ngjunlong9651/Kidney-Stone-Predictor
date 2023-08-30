#!/usr/bin/env python
# coding: utf-8

# In[1]:

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from flask import Flask, render_template, request
from PIL import Image
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns   
st.write("This project was prepared fro Prof Teo # Placeholder text ")
image = Image.open('placeholder-image.jpg')


app = Flask(__name__)

st.subheader('Please enter the relevant details below')
def get_user_input():
    gravity = float(request.form.get("gravity"))
    ph = float(request.form.get("ph"))
    osmo = float(request.form.get("osmo"))
    cond = float(request.form.get("cond"))
    urea = float(request.form.get("urea"))
    calc = float(request.form.get("calc"))
    prediction = -0.04191465 + (gravity * -3.94579654e-02) + (ph * -3.94579654e-02) + (osmo * 3.05883681e-04) + (cond * -8.53476004e-02) + (urea * 1.12604054e-03) + (calc * 7.20512124e-01)
    return prediction



# In[ ]:




