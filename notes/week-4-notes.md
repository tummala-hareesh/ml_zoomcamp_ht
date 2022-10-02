# Week-4
These notes prepared during week-4 of ML Zoomcamp. 

# 1 Evaluation metrics: session overview
- Churn prediction - model to predict customers leaving the company - accuracy = 80%
- What does't the accuracy metric mean? 
- Are there other metrics to evaluate our binary classificaiton model? 
- `Metric` is a function that compares the predictions with the actual values and outputs in a single number that tells how good the predictions are

- Accuracy and Dummy models 
- Other metrics 
    - Confusion table 
    - Precision and Recall 
    - ROC curve
    - ROC-AUC 
    - K-fold Cross Validation 

# 2 Accuracy and dummy model
- Evalute the model on different thresholds 
- Check the accuracy of dummy baselines

- `Accuracy` tells us about fraction of correct predictions. 
- `Accuracy` = No. of correct predictions / No. of total predictions made
- Scikit learn has a metric called `accuracy_score` which does exactly the same as above 
- `Logistic  Regression` optimizes and gives the threshold that gives best accuracy , here it's 0.5
- `Accuracy` doesn't completely give us informatino about Churning and Non-churning 
    - Model will be correct only for non-churning customers
    - For churning ones, it becomes wrong predictions
    - `Class imbalance`  = No. of non-churing customers > No. of chruning customers 

# 3 Confusion table
- Different way of evaluting the model that will not be impacted by `class imbalance`
- g(xi) ~ predict (churn if >= t else no churn)
- If customer churned, send promo email, else none 
- For Prediction = NO Churn, **(NEGATIVE)**
    - Customer didn't churn (correct) - `TRUE NEGATIVE`
    - customer did churn (not correct) - `FALSE NEGATIVE`
    - Negative class
- For Predciction = churn, **(POSITIVE)**
    - Customer didn't churn (not correct) - `FALSE POSITIVE`
    - customer did churn (correct) - `TRUE POSITIVE`
    - Postive class
- Python implementation of TP, TN, FP, FN for confusion table
- % of prediction in confutoin matrix
- Accuracy = TP + TN 

# 4 Precision and Recall
- Precision - Fraction of positive predictions that are correct? 
- Recall - Fraction of churning users that we identified correctly
- Accuracy can be misleading especially when class imbalances are there


# 5 ROC Curves
- ROC - Receiver Operator Characteristicsm
- WW-2 Radar detectors
- `FPR` = False Positive Rate
- `TPR` = True Positive Rate
- ROC curve looks at all the possible thresholds (FPR Recall)
- randome model 
- Ideal model 
- TPR vs FPR - model shouldn't go below random baseline
- Can use scikit-learn to plot ROC curve


# 6 ROC AUC
- 


# 7 Cross-Validation

# 8 Summary

# 9 Explore more

# 10 Homework
