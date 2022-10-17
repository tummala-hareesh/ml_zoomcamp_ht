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
- Previous lesson, training decision trees with sklearn
- Allowing DT to grow indefinitely will cause `overfitting` and model doesn't `generalize`
- While seeting the max_depth parameter will show better results. 

## Finding the best split for DT 
- Pseudo code for best split algo for DT - `Misclassification`
```
    for F in features:
        find all thresholds for F
            for T in thresholds:
                split dataset using "F>T' condition
                compute the impurity of this split 
    
    Select the condition with lowest impurity
```
- Other Classification criteria
    - `Gini`
    - `Entropy`

## How do we know when to stop DT split? 
- If group is already `pure`, don't split
- Tree reached the depth limit  - max_depth
- If min size of group is too small to split

## Review of DT learning Algo 
- Find the best split as 
- Stop if max_depth is reached
- If left is sufficiently large and left not pure 
    - Repeat on left 
- If right is sufficiently large and right not pure 
    - Repeat on right 

# More reading on DTs sklearn
- https://scikit-learn.org/stable/modules/tree.html
- https://mlu-explain.github.io/decision-tree/
- DTs - `non-parametric supervised learning method`
- tree = `piece-wise constant approximation`
- deeper tree = `more complex the decision rules and the fitter the model`
## Advatnages of DTs
- Simpler to understand and to interpret
- Trees can be visualized
- Little data preperation; Other techniques require data normalization, dummy varibles need to be created and blank values to be removed etc.,
- Able to handle both numerical and categorical data; scikit-learn doesn't support categorical for now
- Able to handle multi-output problems
- white box model - observability in the model - explanability 
- Possible to validate the model using statistical tests - account for reliability of the model 
- PErforms weel even if tis assumptions are voilated

## Disadvantages of DTs
- Over-complex tree - overfitting
- Unstable because small variations in the data - different tree
- Piece-wise approximation - not good at extrapolation
- Local optimal vs global optimal problem
- DTs create bias if some classes dominate - need to balance the dataset prior to fitting the DT

## Export trees 
- Graphviz 
- Text format

## Complexity 
- Balanced Binary tree = O(n_samples n_features log(n_samples))
- Query time  = O(log(n_samples)

## Classification criteria
- `Gini` =  SUM_k(p_mk(1-p_mk))
- `Entropy` or `Log Loss`= -SUM_k(p_mk log(p_mk))
    - Shannon entropy = minimizing log loss
    - also called cross-entropy and multinominal deviance 
- `MSE or L2 error`, Poisson deviation `MAE or L1 error` 

- `Minimal cost-complexity Pruning` - prune a tree to avoid over-fitting - provides parameters such as `min_smaples_leaf` and `max_depth`  and `ccp_alpha` cost complextity alpha parameter to control the size of the tree.
    - > `ccp_alpha` increase the no. of nodes pruned


# 5 Decision trees parameter tuning
- Important Parameters to control DT
    - `max_depth`
    - `min_samples_leaf`
- Tune `max_depth` parameter and then tune other parameter
- pivot DF for heatmap creation
- Heatmap of auc values for different combinations of max_depth and min_samples_leaf
- Finalize a DT with max_depth and min_samples_leaf

# 6 Ensemble learning and random forest
- Random forest
    - Average choice of multiple Experts to give a loan or not
    - Similarly, Average probability of multiple DTs is RF
    - Randomness comes from the fact that each DT is different - each model get a random subset of features 
- mutiple independent DTs -> Combine into one taking average
- Traing models is a `Parallel` process

# 7 Gradient boosting and XGBoost
- Different way of comibing multiple DTs = `Boosting`
- Train multiple DTs; Each model corrects mistakes of next model; 
- Training is a `Sequential` process
- IN Boosting, 
    - Data -> Model1 -> Pred1
    - Errors of Model1 -> Model2 -> Pred3
    - Errors of Model2 -> Model3 -> Pred4
    - ....
    - Final Prediction 
- Library = `XGBOOST`
```py
pip install xgboost

import xgboost as xgb
```
- Convert data into special datastructure called `DMatrix`.
- xgb_params for xgb.train
- xgb evals can't be taken into as an ouput; use `%capture output` instead
- print(output.stdout) and parse the data
```py
def parse_xgb_ouput(output):
    
    results = []

    for line in output.stdout.strip().split('\n'):

        # split tabs
        num_iter, train_auc, val_auc = line.split('\t')

        # Format 3 values
        num_iter = int(num_iter.strip('[]'))
        train_auc = float(train_auc.strip('train-auc:'))
        val_auc = float(val_auc.strip('val-auc:'))

        results.append((num_iter, train_auc, val_auc))

    df_results = pd.DataFrame(results, columns=['n_iter','train_auc', 'val_auc'])

    return df_results
```

# 8 XGBoost parameter tuning


# 9 Selecting the best model


# 10 Summary


# 11 Explore more


# 12 Homework