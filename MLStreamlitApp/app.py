#app setup and aestetics
import streamlit as st
import pandas as pd

st.title("Machine Learning App")
st.markdown("For this app, you can upload your own dataset, or use the default one. The default dataset is a dataset from Kaggle called 'Ecommerce Customer Behavior Dataset.' The goal of the app is to ...")
# user input their own file or use default
options = ["Use default data", "Upload your own data"]
choice = st.selectbox("Choose an option:", options, index=None, placeholder = "Select an option")

if choice is not None:
  if choice == "Upload your own data":
    uploaded_file = st.sidebar.file_uploader("Upload your own data", type=["csv"])
    if uploaded_file is not None:
      df_consumers = pd.read_csv(uploaded_file)
    else:
      st.stop()
  else:
    df_consumers = pd.read_csv("eCommerce-dataset.csv")

  target_column = st.selectbox(
      "Select a target column:", df_consumers.columns)