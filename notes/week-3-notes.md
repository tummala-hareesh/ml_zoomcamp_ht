# Week-3
These notes prepared during week-3 of ML Zoomcamp. 


# 1 Churn prediction project
- Telecom company - customers/clients
- Happy/Unhappy customers 
- Clients who want to leave the company - Move to competitor
- Assign score from 0 to 1, to identify customers who churn
- Promotinal offers to customers who plan to churn 
- No discounts to customers who stay 
- Way to approach this problem using ML ~ `Binary Classification`
    - g(xi) ~ yi
    - i = customer
    - yi  = [0,1]; No churn - Churn
- Output of the model = score between 0-1 - `Likelihood of Churn`
- Historical data of customers to build ML binary classification model
- [Kaggle dataset = Telco-Customer-Churn](https://www.kaggle.com/c/customer-churn-prediction-2020)


# 2 Data preparation
- Download data; use pandas to read the data; and pre-processing 
- `wget` to download data
- Standardize column names and categorical feature data
- Change wrong object features into float values 
- change `churn` feature into binary variable.

# 3 Setting up the validation framework
- Create test-validation-train datasets using sklearn
- Load train_test_split function from sklearn 
- Use `?` after train_test_split to get documentation details about the function/method 
- Getting full_train , test datasets is strainghtfoward with the use of test_size=0.2
- But, for train, val split on full_train, we should use test_size=0.25 because 
    - 20%/80% = 25%
- Create y_train, y_val, and y_test lists
- Delete Target variables (churn) from df_train, df_val and df_test

# 4 EDA
- 


# 5 Feature importance: Churn rate and risk ratio

# 6 Feature importance: Mutual information

# 7 Feature importance: Correlation

# 8 One-hot encoding

# 9 Logistic regression

# 10 Training logistic regression with Scikit-Learn

# 11 Model interpretation

# 12 Using the model

# 13 Summary

# 14 Explore more

# 15 Homework
