#----------------------------------------------------------------------------------------------------------------------------------------------
#app setup and aestetics
#----------------------------------------------------------------------------------------------------------------------------------------------
import os

import streamlit as st
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import altair as alt
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

st.title("Machine Learning App")
st.markdown("For this app, you can upload your own dataset, or use the default one. The default dataset is a dataset from Kaggle called 'Ecommerce Customer Behavior Dataset.' " \
"The goal of the app is to test how well a machine learning model can predict a numeric outcome from any dataset")

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
        csv_path = os.path.join(os.path.dirname(__file__), "eCommerce-dataset.csv")
        df_consumers = pd.read_csv(csv_path)
else:
    st.stop()

#filtering so only numeric columns can be selected
numeric_cols = df_consumers.select_dtypes(include="number").columns
target_column = st.selectbox("Select a target column:", numeric_cols)

#----------------------------------------------------------------------------------------------------------------------------------------------
#making the regression plot
#----------------------------------------------------------------------------------------------------------------------------------------------

#first cleaning data
df_clean = df_consumers.dropna()
y = df_clean[target_column]
X = df_clean.drop(columns=[target_column])
X = pd.get_dummies(X, drop_first=True)

#splitting into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

#allowing the user to adjust the alpha level
st.markdown("### Adjust the alpha level")

st.markdown(f"""
**Changing the alpha level in a regression impacts how strict the model is:**
* A **higher** alpha level means the model will be more strict.
* A **lower** alpha level means the model will be more lenient and consider variables that have weaker evidence.

****Note**: An alpha level can be thought of as a bar set for convincing evidence when looking to see whether a variable is important in predicting the target. """)

alpha = st.select_slider(
    "Alpha level:",
    options=[0.0, 0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0],
    value=1.0,)

model = Ridge(alpha=alpha)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# finding R and RMSE
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5

#----------------------------------------------------------------------------------------------------------------------------------------------
#explanations and displays
#----------------------------------------------------------------------------------------------------------------------------------------------

#Displaying the R and RMSE scores (largely)
st.subheader("Model Performance on Test Data")
col1, col2 = st.columns(2)
col1.metric("R² Score", f"{r2:.3f}")
col2.metric("RMSE", f"{rmse:.2f}")

# Plain-language explanations of each metric
st.markdown(f"""
**What these metrics mean:**""")
st.markdown(f""" **R² Score**: Measures the variation in **{target_column}** that the model successfully explains. A R² of **1.0** means stronger predictions, a **0** means the model is no better than guessing the average.""")
st.markdown(f"""**RMSE**: Shows how much better or worse the model is at predicting actual values.""")
st.markdown(f"""
* Low RMSE: The model's predictions are close to the actual ones.
* High RMSE: The model's predictions are far off from the actual ones.
""")

#----------------------------------------------------------------------------------------------------------------------------------------------
# Creating the scatter plot
#----------------------------------------------------------------------------------------------------------------------------------------------
st.subheader(f"Actual vs. Predicted: {target_column}")
results_df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})

scatter = (
    alt.Chart(results_df)
    .mark_circle(size=60, opacity=0.7)
    .encode(
        x=alt.X("Actual", title=f"Actual {target_column}"),
        y=alt.Y("Predicted", title=f"Predicted {target_column}"),
        tooltip=["Actual", "Predicted"],))

# Adding the red line of best fit (perfect predictions)
min_val = float(min(results_df["Actual"].min(), results_df["Predicted"].min()))
max_val = float(max(results_df["Actual"].max(), results_df["Predicted"].max()))
line_df = pd.DataFrame(
    {"Actual": [min_val, max_val], "Predicted": [min_val, max_val]})
perfect_line = (
alt.Chart(line_df)
    .mark_line(color="red", strokeDash=[5, 5])
    .encode(x="Actual", y="Predicted"))

st.altair_chart(scatter + perfect_line)
st.caption("Points closer to the red dashed line represent more accurate predictions.")
