from json import load
from xmlrpc.client import Boolean
import streamlit as st
import pandas as pd
import numpy as np
import time 
import matplotlib.pyplot as plt
from multiapp import MultiApp
from Apps import asg1, asg2, asg3, asg5, asg6 , asg7 , asg8

#variables
disrad = False

st.title("Data Mining Tool")

file = st.file_uploader("Enter Dataset first to Proceed", accept_multiple_files=False,disabled=False)
# data = pd.read_csv(file)

def load_file():
    df = pd.read_csv(file)
    st.header("Dataset Table")
    st.dataframe(df, width=1000, height=500)
    return df
if file:
    data = load_file()  
    
    app = MultiApp()
    
    app.add_app("ASG1. Measures of Central tendency, Dispersion, Plots", asg1.app)
    app.add_app("ASG2. Chi Sqaure test, Correlation and Normalization", asg2.app)
    app.add_app("ASG3&4. Info Gain, Gini,Extract Rules, Decision Tree ", asg3.app)
    # app.add_app("ASG4. Extract Rules, Confision matrix", asg4.app)
    app.add_app("ASG5. Regression classifier, KNN, ANN", asg5.app)
    app.add_app("ASG6. Hiechical Clustering,AGNES ,DSCAN,K-Means,K-medoids" , asg6.app)
    app.add_app("ASG7. Apriori" , asg7.app)
    app.add_app("ASG8. Crawler , Page Rank",asg8.app)
    # The main app
    app.run(data)

