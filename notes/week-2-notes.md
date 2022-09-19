# Week-2
These notes prepared during week-2 of ML Zoomcamp. 

# 1 Car price prediction project
- Develop a model to help user predict car price. 
- Dataset from Kaggle - [Car Features and MSRP](https://www.kaggle.com/datasets/CooperUnion/cardataset)
- Project Plan 
    - Preapre data and do EDA 
    - Use linear regression for predicting price
    - Use the internal of linear regression 
    - Evaluting the model with RSME 
    - Feature Engineering 
    - Regularization 
    - Using the model 

# 2 Data preparation
- [Notebook](../ipynb/02_car_price_prediction.ipynb)
- Standardize column names
- Standardize categorical features  

# 3 Exploratory data analysis
- How data the looks like?
- Get a feeling about the data
- All MSRP = distribution using `histogram`
    - Long tail = `- Not good for ML`
    - `Solution` - Apply **log**
        - log will scale larger values 
        - issue is that log(0) is undefined = Add `+1` to all data
            - `log1p` - shortcut to add 1 and takes log
- MSRP distribution of cars MSRP < 1000000
- log-MSRP now looks more like `Normal Distribution`
- ML models do better with normal distribution 
- Check if there are missing values in the dataset.


# 4 Setting up the validation framework
- For validating model, split dataset into test-val-train
- Split using length of dataframe ; make sure not to omit any records
- Sequential splits should not be used; Shuffle the dataset first before splitting sequentially
- random seed to reproduce the split using `np.random.shuffle()`
- check for different index in the split dataframe

# 5 Linear regression
# 6 Linear regression: vector form
# 7 Training linear regression: Normal equation
# 8 Baseline model for car price prediction project
# 9 Root mean squared error
# 10 Using RMSE on validation data
# 11 Feature engineering
# 12 Categorical variables
# 13 Regularization
# 14 Tuning the model
# 15 Using the model
# 16 Car price prediction project summary
# 17 Explore more
# 18 Homework
