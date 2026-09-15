import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.")

if st.button('Click me'):
    st.write('Button clicked!')
else:
    st.write('Button not clicked yet.')


import pandas as pd

st.subheader("Exploring Our Dataset")
df = pd.read_csv("data/sample_data.csv")

# if in week_2 or somewhere else, still do pd.read.csv("") but use "./Week_2/sample_data.csv"

st.write("Here's our data")
st.dataframe(df)

city = st.selectbox("Select a city", df["City"].unique())
st.write(f"People in {city}")
st.dataframe(df[df["City"]== city])

st.bar_chart(df["Salary"])