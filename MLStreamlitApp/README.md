Simply put, the purpose of this app is to test how well a machine learning model can predict a numeric outcome from any dataset. For more details, refer to the frequently asked questions section.

------------------------------------------------------------------------------------
**How to access the app**
------------------------------------------------------------------------------------

**Running the app locally:**
Use this link: https://emerson-data-science-portfolio-zneyhhdgm5zczjdraqztwc.streamlit.app/ if there are issues, follow the steps below:

1. Download or clone the repository onto your own device through github
2. Install the required libraries (refer to requirements.txt)
3. Use the terminal command to run the app in a browser: streamlit run app.py

**Link to deployed app:** 
https://emerson-data-science-portfolio-zneyhhdgm5zczjdraqztwc.streamlit.app/ 

**Libraries needed with versions:**
* streamlit==1.48.0
* pandas==2.3.1
* scikit-learn==1.9.1
* matplotlib==3.10.0

**Model Used:** Ridge Regression (a linear regression model)

**Hyperparameter:** The alpha slider

------------------------------------------------------------------------------------
**References**
------------------------------------------------------------------------------------
Here are some references I used in research and while coding this app:
* https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf
* https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html
* https://jbhender.github.io/Stats506/F17/Projects/G13/Python.html 

------------------------------------------------------------------------------------
**Here are some "frequently asked questions" that could be beneficial in understanding the capabilites of this app:**
------------------------------------------------------------------------------------

**What is this regression model?**
This multiple regression model is called a Multiple Ridge Regression. It is a type of multiple linear regression that uses an alpha level to prevent overfitting. The word “ridge” accounts for the fact that there are many potential columns that can be regressed all at once for a single numeric target. It is also beneficial to prevent multicollinearity (heavily correlated independent variables) since it adds shrinkage.

**What does this do for the user?**
Based on the dataset given (default or uploaded), it predicts the outcomes of the column the user chooses. This is the second choice made in the app. Then, the user gets to choose how strict the model will be, and whether it will ignore noisy variables through their choice on the alpha slider. 

**Why use Ridge as a hyperparameter over KNN or a decision tree?**
I was not sure how to best accommodate the amount of columns in a potential dataset for this app. There was no doubt that I wanted to use a regression model for this app, and I believed a scatterplot with a best fit line would best show the accuracy of what could be built through the code. When thinking about the hyperparameter, I worried about the downsides of using a decision tree since it can easily overfit. As for KNN, we learned that the calculations on geometric differences between rows can be messy with too large of a dataset. Since a requirement was that the user could have the option to upload their own dataset, I felt it was not worth the risk of KNN or overfitting with a decision tree, even though those hyperparameters can find nonlinear patterns. After some quick research, I felt ridge would be best. Even though I would be giving up finding non linear patterns, ridge would provide an opportunity to learn a new hyperparameter, while also keeping a lot of code similar to what I am familiar with from class from the regression unit. The biggest difference is the addition of pd.get_dummies, which I explain in another question dropdown.

**What does the math from regressing show?**
What we are given from the regression is the two most important metrics to understand the success of the model: RMSE and R-squared. The R-squared measures the variation in target variable that the model successfully explains. The RMSE shows how much better or worse the model is at predicting actual values. More in depth explanations can be found on the app. 

**How does the math translate to the plot?**
Each blue dot compares an observation’s real value on the x axis, to the equation's predicted value on the y axis. Blue dots on or very close to the red dashed line mean accurate guesses, while a flat horizontal band of blue dots shows that the model couldn't find a strong pattern.

**What is the difference between what pd.get_dummies is filtering and the filtering of numeric target categories?**
In the code, we have to filter target categories (y) because linear regression is limited to columns with numbers. For that reason, the user can only select from columns where the observations are numbers. However, this gets confusing because pd.get_dummies is able to convert predictors (x) to numbers, even if the columns contain categorical observations. Once the user selects a column in the dataset, pd.get_dummies collects the full dataset for the regression against the target column.

**What can a user do with this app?**
This app allows users to upload any CSV dataset of their choosing to train and analyze a Ridge Regression model without writing code of thier own to fit the dataset. It can be beneficial since it can quickly test whether features in the dataset can accurately predict a chosen outcome.

