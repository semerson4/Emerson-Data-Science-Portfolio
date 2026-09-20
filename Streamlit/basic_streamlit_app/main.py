import pandas as pd           
import seaborn as sns          
import matplotlib.pyplot as plt  
import streamlit as st  

#Titling and description for the app
st.title("World Happiness Report")

#Python read the files
2015 = pd.read_csv("data/2015.csv")
2016 = pd.read_csv("data/2016.csv")
2017 = pd.read_csv("data/2017.csv")
2018 = pd.read_csv("data/2018.csv")
2019 = pd.read_csv("data/2019.csv")

heatmap_data = pd.concat([2015, 2016, 2017, 2018, 2019], axis=0)
