# Week-3
These notes were prepared during week-3 of ML Zoomcamp. 


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
- Look for missing values and fix them 
- Look at target variable - `churn`
    - Use `df.value_counts(normalize=True)` to get % data
    - Churn Rate is defined as `#of ones/n` for the feature
    - Churn Rate ~ 26%
- Look at numerical and categorical variables 

# 5 Feature importance: Churn rate and risk ratio
- Churn Rate - Global vs Male vs Female ~ similar 
- Churn Rate - Global vs no partner vs partner - not similar
    - 5% more for no partners wrt global
    - 6% less for partners wrt global  
- Above EDA details gives us an idea about `feature importance`
- Difference = Global - Group 
    - Difference<0 = More likely to Churn
    - Difference>0 = Less Likely to Churn 
- Instead of difference, we can look at division  = `Risk Rate`
    - Risk Rate = Group / Global 
    - RR > 1; Customer higher risk to Churn 
    - RR < 1; Customer at lower risk to churn
- Instead of doing above for each feature, we use SQL to create new table of churn rates
```py
SELECT 
    gender, 
    AVG(churn),
    AVG(churn) - global_churn AS diff,
    AVG(churn) / global_churn AS risk 
FROM 
    data
GROUP BY 
    gender;
```
- Or using pandas 
```py
df.groupby('gender').churn.mean()
```
- We now know if the feature is important to predict churn or not. 
- But, if we have ranks for each feature to identify importance (order of importance), then that will be helpful.


# 6 Feature importance: Mutual information
- Way to measure importance of categorical features. 
- `Mutual information` - concept from information theory
    - how much we learn about one variable if we know value of another
- sklearn has `mutual_info_score` package for us to use
- 'contract' is most important and 'gender' is least important
- High MI score = important - good indicators for ML models
- Models looks for these patterns 

# 7 Feature importance: Correlation
- Measuring the Importance of numerical features
- `Correlation coefficient` - measures the degree of dependency between 2 variables. 
- Tenure - negative correlation 
- Monthly Charges - positive correlation 

# 8 One-hot encoding
- Feature variables into individual binary variables 
- feature_extraction - DictVectorizer


# 9 Logistic regression
- Binary Classification ~ [0,1]
- g(xi) ~ yi
- SIGMOD function 
    - ```py
        def sigmod(z):
            return 1/(1+np.exp(-z))
    ``` 
- Linear vs Logistic regression formulations 

# 10 Training logistic regression with Scikit-Learn
- Train a model using scikit-learn
- apply to validation dataset
- Calculate accuracy 
- Hard preditions using `predict`
- Probability predictions uisng `predict_probab`
- Accuracy measurements

# 11 Model interpretation
- Look at the coefficients 
- Train a smaller model with fewer features 


# 12 Using the model
- full train dataset
- test datasets 
- accuracy = 81%
- Testing it on 1 customer and comparing aginst y_test


# 13 Summary
- Feature importance - risk, mutual information, correlation 
- One-hot encoding using `DictVectorizer`
- LogisticRegression 
- Ouput of log reg - probability 
- Interpretation of weights is similar to linear regression 


# 14 Explore more
- Exclude least useful features 
- Instead of Linear Regression (not regularized), Ridge Regression (regularized)
    - Find the best regualization parameter of Ridge
- Other ways of OneHotEncoding
- Check how to use StandardScaler 

## Additional Projects
- Lead scoring - https://www.kaggle.com/ashydv/leads-dataset
- Default prediction - https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients


# 15 Homework
- [Notebook to homework](./../ipynb/03_homework.ipynb)