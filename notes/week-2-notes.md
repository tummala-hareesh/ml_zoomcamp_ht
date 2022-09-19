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
- Solving regression problems
- `g(X) ~ y`
- [Youtube video](https://www.youtube.com/watch?v=Dn1eTQLsOdA&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=16)

# 6 Linear regression: vector form
- `linear regression = w0 + dot(xi + w)`
- `linear_regression = X.dot(w_new)`
- [Youtube video - vector form](https://www.youtube.com/watch?v=YkyevnYyAww&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=17)


# 7 Training linear regression: Normal equation
- For some an exact solution mayn't exist, so, a generalized solution is to find approximate solution.
-  [Approx. form](https://www.youtube.com/watch?v=hx6nak-Y11g&list=PL3MmuxUbc_hIhxl5Ji8t4O6lPAOpHaCLR&index=18)
```py

def train_linear_regression(X, y):
    ones = np.ones(X.shape[0])
    X = np.column_stack([ones, X])
    
    XTX = X.T.dot(X)
    XTX_inv = np.linalg.inv(XTX)
    w_full = XTX_inv.dot(X.T).dot(y)
    
    return w_full[0], w_full[1:]

```

# 8 Baseline model for car price prediction project
- Filter numerical columns from dataset
- Build model using those columns 
- Comparing results using histogram 
- Metric needed to estimate if the model is performing better or not?


# 9 Root mean squared error
- RSME = root mean squared error 
- g(xi) = prediction for xi
- yi = actual value for xi
- RSME = SQRT((SUM(g(xi) - yi)^2)/n)

# 10 Using RMSE on validation data
- Train the model using `training dataset`
- apply predictions on `validation dataset`
- estimate `rsme` on validation datawset

# 11 Feature engineering
- Create a new columns called `age` using `year` of car manufactured
- Re-train the model and check rsme
- There is a sifnificant improvement in rsme. 
- So, MSRP depends on age of the car.

# 12 Categorical variables
- categorical variables = strings = object types 
- `number of doors` is categorical 
- Use categorical variables for ML model 
- Typical way of encoding 
    - New Binary columns for each value in main column 
- No. of doors doesn't improve the model by much 
- `Make` of the car improves the model by 1%
- Adding more (all) categorical variables makes the model worse. 

# 13 Regularization
- Why is RSME so high after adding cat variables?
    - When inverse doesn't exists
    - Data is not super clean 
    - Add a tiny number to data to get solution - non-singular matrix
    - Larger the tiny  number added to diagonal = more control we get
- `5%` improvement - by controlling the value
- regularization r is a parameter ot the model 


# 14 Tuning the model
- Try to find the best value of r (regulization parameter) for our model
- For r=0.0 regulization the score is bad 
- For r>1.0, the score again worsens

# 15 Using the model

# 16 Car price prediction project summary

# 17 Explore more

# 18 Homework
