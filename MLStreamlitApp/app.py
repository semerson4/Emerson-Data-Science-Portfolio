#app setup and aestetics
import streamlit as st
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
import altair as alt
from sklearn.metrics import mean_squared_error, r2_score

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
else:
  st.stop()

numeric_cols = df_consumers.select_dtypes(include="number").columns
target_column = st.selectbox("Select a target column:", numeric_cols)

df_clean = df_consumers.dropna()
y = df_clean[target_column]
X = df_clean.drop(columns=[target_column])
X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

#not sure if i want to keep this
alpha = st.slider(
    "Regularization Strength (alpha):",
    min_value=0.0,
    max_value=10.0,
    value=1.0,
    step=0.5,)

model = Ridge(alpha=alpha)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

#not sure abt this either
r2 = r2_score(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5

st.subheader("Model Performance on Test Data")
col1, col2 = st.columns(2)
col1.metric("R² Score", f"{r2:.3f}")
col2.metric("RMSE", f"{rmse:.2f}")

# Plain-language explanations of each metric
st.markdown(f"""
**What these metrics mean:**
* **R² Score ({r2:.3f}):** Measures how much of the variation in **{target_column}** the model successfully explains. A score closer to **1.0** means stronger predictions, while a score near **0** means the model is no better than guessing the average.
* **RMSE ({rmse:.2f}):** Root Mean Squared Error—the typical size of the model's prediction errors, measured in the exact same units as **{target_column}**. Lower numbers mean closer predictions.
""")

# 6. Actual vs. Predicted scatter plot
st.subheader(f"Actual vs. Predicted: {target_column}")
results_df = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})

scatter = (
    alt.Chart(results_df)
    .mark_circle(size=60, opacity=0.7)
    .encode(
        x=alt.X("Actual", title=f"Actual {target_column}"),
        y=alt.Y("Predicted", title=f"Predicted {target_column}"),
        tooltip=["Actual", "Predicted"],
    )
)

# Red dashed diagonal line showing where perfect predictions would fall
min_val = float(min(results_df["Actual"].min(), results_df["Predicted"].min()))
max_val = float(max(results_df["Actual"].max(), results_df["Predicted"].max()))
line_df = pd.DataFrame(
    {"Actual": [min_val, max_val], "Predicted": [min_val, max_val]})
perfect_line = (
    alt.Chart(line_df)
    .mark_line(color="red", strokeDash=[5, 5])
    .encode(x="Actual", y="Predicted"))

st.altair_chart(scatter + perfect_line)
st.caption(
    "Points closer to the red dashed line represent more accurate predictions.")