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
- Useful metric for binary classification 
- AUC = Area Under the ROC Curve
- ROC curve -  close of ideal point (1.0)
- Another way to quantiy above is area under the curve 
- AUC > Great performing model 
- For ideal curve, AUC =1.0
- For random curve, AUC =0.5
- Our model, AUC > 0.5 and <= 1.0
- sklearn - `auc` - area under any curve; `roc_auc_score` - computes area under the curve from y_val, y_pred
- How well AUC seperates negative from positive examples. 


# 7 Cross-Validation
- Parameter tuning for selecting best parameter of our model 
- Full train and test - split into parts (k=3) - train and evaluate model - compute mean and std
- `pip install tqdm` to track progress of kfold cross validation
- In `Logistic Regression`, C is regularization parameter 

# 8 Summary
- Metric - a single number that describes performance a model 
- Accuracy - fraction of correct answers, metric can be misleading sometimes
- Precision and Recall - are less misleading when we have class imbalance
- ROC curve - a way to evalute the performance at all thresholds; works with class imbalance too
- K-fold CV - more reliable estimate for performance (mean + std); parameter tuning 

# 9 Explore more
- F! score 
- Evalute prevision and recall at different thresholds, plot P vs R 
- AUC 
- `Other projects`
    - Calcuate the metrics for datasets from the previsou week 

# 10 Homework
- [Link to Notebook](./../ipynb/04_homework.ipynb)