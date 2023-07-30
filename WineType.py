# Importing the needed libraries
import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# Loading in the file
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

# Givinig an introduction
st.title("Wine Type Prediction")
st.markdown("This application allows a user to input in 13 qualities typically found within wine." 
            "The app will then predict whether the wine is either a white wine or red wine."
            "The qualities that will be used to judge the type are as follows:"
            "Fixed acidity, volatile acidity, citric acid,"
            "residual value, sugar chlorides, free sulfur dioxide,"
            "total sulfur dioxide, density, ph,"
            "sulphates, alcohol, quality")


# Defining the terms above
st.markdown("Below tabs are displayed that will define each of the 12 terms defined above. There are 4 parts, with each containing 3 definitions.")
tab1, tab2, tab3, tab4, = st.tabs(["Qualities P1", "Qualities P2", "Qualities P3", "Qualities P4"])

# Setting up tab1
tab1_dict = {"Fixed Acidity" : "This refers to the total amount of non-volatile acids that are present in the wine. "
             "The acids are fixed because they don't dissapate when exposed to heat or air. "
             "These acids play a pivotal role in determining the wine's taste, aging, and structure.",
             "Volatile Acidity" : "Volatile acids are similar to non-volatile acids, except they do disappate when exposed to heat or air. "
             "These acids are responsible for the various types of aromas and flavors in the wine. ",
             "Citric Acid" : "Citric acid is an organic acid that is typically present in fruits. "
             "While citric acid is found in grapes, it is not as prevelent in wines as the previous acids, but does enhance the wine's freshness. "}
tab1_keys = list(tab1_dict)
with tab1:
    st.subheader("Part 1 Words")
    sub_tabs = st.radio("Choose an option to see its definition", tab1_keys)
    if sub_tabs in tab1_dict:
        st.subheader(sub_tabs)
        st.markdown(tab1_dict[sub_tabs])

# Setting up tab2
tab2_dict = {"Residual Value" : "In terms of the wine, this refers to the leftover grape sugars that remain in the wine after fermentation is complete. "
             "It could also mean residual alcohol, which is when a distilled spirit (such as brandy) is added to the wine to increase its alcohol content and halt fermentation.",
             "Chlorides" : "In terms of winemaking, chlorides can be found in grapes and the grape juice. "
             "The chlorides help influence the taste and sensory effects for the wine.",
             "Free Sulfur Dioxide" : "This refers to the form of sulfur dioxide gas that isn't bound to anything and is in its gaseous state. "
             "Sulfur dioxide helps prevent oxidation, which can cause the wine to spoil. This greatly helps the wine's quality"}
tab2_keys = list(tab2_dict)
with tab2:
    st.subheader("Part 2 Words")
    sub_tabs2 = st.radio("Choose an option to see its definition", tab2_keys)
    if sub_tabs2 in tab2_dict:
        st.subheader(sub_tabs2)
        st.markdown(tab2_dict[sub_tabs2])

# Setting up tab3
tab3_dict = {"Total Sulfur Dioxide" : "This refers to the total amount of sulfur dioxide in the wine, both unbound and bound. "
             "The total sulfur dioxide concentration is essential for winemakers to ensure that the wine is adequately protected from spoilage while avoiding excessive use of SO2,"
             " which could lead to undesirable sulfur faults in the wine.",
             "Density" : "For the wine, density can mean multiple things. It could mean the grape density (number of grapes per unit), "
             "or the juice density, which means the sugar content in the grape juice before fermentation.",
             "pH" : "pH means potential of hydrogen. It is a measure of acidity or alkalinity in the solution. "
             "It helps balance the acids out in the wine, and makes the sulfur dioxide more effective"}
tab3_keys = list(tab3_dict)
with tab3:
    st.subheader("Part 3 Words")
    sub_tabs3 = st.radio("Choose an option to see its definition", tab3_keys)
    if sub_tabs3 in tab3_dict:
        st.subheader(sub_tabs3)
        st.markdown(tab3_dict[sub_tabs3])

# Setting up tab4
tab4_dict = {"Sulphates" : "This refers to sulfur dioxide (SO2) or sulfites, which are sulfur-containing compounds used as additives in winemaking. "
             "Sulphates are important for maintaining wine quality and stability.",
             "Alcohol" : "In winemaking, alcohol refers to ethyl alcohol or ethanol, which is the primary alcohol produced during the fermentation process. "
             "Alcohol has a significant impact on a wine's taste, body, and mouthfeel.",
             "Quality" : "This encompasses various factors contributing to the overall excellence, appeal, and integrity of the wine. "
             "Measuring it requires both objective and subjective assessments. A few types of methods to measure it are sensory evaluation and chemical analysis."}
tab4_keys = list(tab4_dict)
with tab4:
    st.subheader("Part 4 Words")
    sub_tabs4 = st.radio("Choose an option to see its definition", tab4_keys)
    if sub_tabs4 in tab4_dict:
        st.subheader(sub_tabs4)
        st.markdown(tab4_dict[sub_tabs4])

st.header("Wine Type Predictor: White or Red")

st.markdown("Input your value in the text boxes below. When you're ready, press predict.")
fixed_acidity = st.text_input("Enter the fixed acidity")
volatile_acidity = st.text_input('Enter the volatile acidity')
citric_acid = st.text_input("Enter the citric acid")
residual = st.text_input("Enter the residual value")
chlorides = st.text_input("Enter the sugar chlorides")
free_sulfur_dioxide = st.text_input("Enter the free sulfur dioxide value")
total_sulfur_dioxide = st.text_input("Enter the total sulfur dioxide value")
density = st.text_input("Enter the density value")
pH = st.text_input("Enter the ph value")
sulphates = st.text_input("Enter the value of the sulphates")
alcohol = st.text_input("Enter the alcohol value")
quality = st.text_input("Enter the quality number")
result =" "
      
# Running the model
def prediction(fixed_acidity, volatile_acidity, citric_acid, residual, chlorides,	free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality):     
    prediction = classifier.predict([[fixed_acidity, volatile_acidity, citric_acid, residual, chlorides,	free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality]])
    return prediction
      
  
if st.button("Predict"):
    result = prediction(fixed_acidity, volatile_acidity, citric_acid, residual, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol, quality)
st.success('The output is {}'.format(result[0]))
