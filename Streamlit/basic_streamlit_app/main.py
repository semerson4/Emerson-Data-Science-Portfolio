import pandas as pd           
import seaborn as sns          
import matplotlib.pyplot as plt  
import streamlit as st  
import plotly.express as px


#Python read the files
df_2015 = pd.read_csv("data/2015.csv")
df_2016 = pd.read_csv("data/2016.csv")
df_2017 = pd.read_csv("data/2017.csv")
df_2018 = pd.read_csv("data/2018.csv")
df_2019 = pd.read_csv("data/2019.csv")


#Making a sidebar for organization-------------------------------------------------
st.sidebar.header("Visualizations")
page = st.sidebar.radio("Go to:", ["Homepage", "World Map Heatmap", "All Data Chart"])

#Page 1: Intro page ---------------------------------------------------------
if page == "Homepage":
    st.title("World Happiness Report")

    st.markdown("""
    
    This Streamlit app is meant to help understand and visualize the World Happiness Report data from 2015 to 2019. The data is sourced from the [World Happiness Report](https://worldhappiness.report/)

    The data sets include variable such as:

    **Country** - This variable identifies the country that a certain level of happiness is associated with.

    **Region** - This variable correlates the country identified with a certain region of the world.

    **Happiness Rank** - This variable identifies the rank of a country as compared with the rest, based on the happiness score. The variable is a numerical value that ranges from 1 to 156, with 1 being the happiest country and 156 being the least happy country.

    **Happiness Score** - This variable identifies the happiness score of a country. The variable is a numerical value that ranges from 0 to 10, with 0 being the least happy and 10 being the happiest country. It is different than the happiness rank in that it is a continuous variable, while the happiness rank is a discrete variable.
    """)

#Page 2: World Map Heatmap---------------------------------------------------------
if page == "World Map Heatmap":
    def load_all_data():
        years = [2015, 2016, 2017, 2018, 2019]
        all_data = []

        for year in years:
            df = pd.read_csv(f"data/{year}.csv")
            df['Year'] = year

            if "Country or region" in df.columns:
                df = df.rename(columns={"Country or region": "Country"})

            if "Happiness Score" in df.columns:
                df = df.rename(columns={"Happiness Score": "Happiness_Score"})
            elif "Happiness.Score" in df.columns:
                df = df.rename(columns={"Happiness.Score": "Happiness_Score"})
            elif "Score" in df.columns:
                df = df.rename(columns={"Score": "Happiness_Score"})

            all_data.append(df[["Country", "Happiness_Score", "Year"]])

        return pd.concat(all_data, ignore_index=True)

    df = load_all_data()
    selected_year = st.selectbox(
        "Select Year",
        options=[2015, 2016, 2017, 2018, 2019],
    )
    df_filtered = df[df["Year"] == selected_year]

    fig = px.choropleth(
        df_filtered,
        locations="Country",
        locationmode="country names",
        color="Happiness_Score",
        hover_name="Country",
        color_continuous_scale=px.colors.sequential.Plasma,
        range_color=[0, 10],
    )

    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0))
    fig.update_layout(margin=dict(l=0, r=0, t=50, b=0))
    st.plotly_chart(fig, use_container_width=True)


#Page 3: All Data Chart---------------------------------------------------------
if page == "All Data Chart":
    st.header("All Data from 2015 to 2019")
    chart_data = pd.concat([df_2015, df_2016, df_2017, df_2018, df_2019], axis=0)

    st.dataframe(chart_data)
    st.set_page_config(layout="wide")
