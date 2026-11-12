#app setup and aestetics
import streamlit as st
import pandas as pd

# user imput their own file or use defailt
options = ["Use default data", "Upload your own data"]
choice = st.selectbox("Choose an option:", options)

if choice == "Upload your own data":
    uploaded_file = st.sidebar.file_uploader("Upload your own data", type=["csv"])
    if uploaded_file is not None:
        df_consumers = pd.read_csv(uploaded_file)
else:
    df_consumers = pd.read_csv("data/consumers.csv")