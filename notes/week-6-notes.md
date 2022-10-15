# Week 6 
These notes were prepared during week-6 of ML Zoomcamp. 

# 1 Credit risk scoring project
- Make decisions on a applicant based on his/her credit score. 
- g(xi) -> prob of default
- Brief about this week
    - Look at dataset
    - data cleaning and prep
    - Decision tree
    - DT algos
    - DT parameter tuning
    - Ensemble and Random forest
    - Gradient Boosting and XGBoost
    - Select best of 3 models 

# 2 Data cleaning and preparation
- Download the [dataset](https://github.com/gastonstat/CreditScoring/raw/master/CreditScoring.csv) using wget
- `head filename.csv` to see first 10 lines of the file - linux command 
- Read the dataset using pandas 
- `Standardize` column names 
- Try to extract meaningful information from different data columns
- `Map column features` as per category data - This is done to have a much better understanding about the dataset.
- Perform EDA on the dataset
- Prepare dataset for modeling

# 3 Decision trees
## How does a decision tree look like? 
- DT is a data structure. 
    - Based on the condition on a `node` - goes left or right branch 
    - Same follows to child nodes
## Training a DT?
- Basically, a bunch of if-else statements used for determining target variable
- Learning rules from the data itself instead of hard-coding if-else logics 

- **Steps:**
    - Turn training `DF` into `list_dict`
    - `list_dict` into `feature matrix`
    - Train DT 
    - AUC for val and train differ a lot

- Overfitting
    - When model memorizes the data; Fails to generalize
    - Depth is `unresitricted`

- Controlling the size of the tree
    - Depth = 3; Learn rules that are less specific
    - Depth = 0; `Decision Stump` - not really a tree; only 1 condition

- Look at rules that DT learned; use export_text from sklearn.tree

# 4 Decision tree learning algorithm


# 5 Decision trees parameter tuning


# 6 Ensemble learning and random forest


# 7 Gradient boosting and XGBoost


# 8 XGBoost parameter tuning


# 9 Selecting the best model


# 10 Summary


# 11 Explore more


# 12 Homework