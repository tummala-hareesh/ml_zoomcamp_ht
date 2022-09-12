# Week-1 
These notes prepared during week-1 of ML Zoomcamp. 

# Table of Contents
1. [Introduction to Machine Learning](#1-introduction-to-machine-learning)
2. [ML vs Rule-Based Systems](#2-ml-vs-rule-based-systems)
3. [Supervised Machine Learning](#3-supervised-machine-learning)
4. [CRISP-DM](#4-crisp-dm)
5. [The Modelling Step (Model Selection Process)](#5-the-modelling-step-model-selection-process)
6. [Setting up the Environment](#6-setting-up-the-environment)
7. [Introduction to NumPy](#7-introduction-to-numpy)
8. [Linear Algebra Refresher](#8-linear-algebra-refresher)
9. [Introduction to Pandas](#9-introduction-to-pandas)
10. [Summary](#10-summary)
11. [Homework](#11-homework)

## 1 Introduction to Machine Learning
- ML using simple example 
    - Buy a used car - Estimate approximate price that doesn't make or break ones financial situation
    - General human way is to examine existing car ads prices and put an estimate.
    - ML is doing the same above using data.
    - Data -> Expert -> Patterns 
    - Data -> ML model -> Patterns
- `Features ` - information about cars
- `Target` - what we are predicting
- `Model` - train a model; encapsulate all patterns identified from data
- Feature + Model = Predictions 

## 2 ML vs Rule-Based Systems
- E.g: Email spams
- Build a Classifier that filters SPAM emails
    - From a sender - promotions@online.ca
    - From a domain - online.com 
    - Keywords - funding, money, taxes, etc., 
- `Rule based systems` - limitation - more code - keywords to filter spams 
- `ML way to solve the problem`
    - Get data
        - Use **SPAM** folder to filter spam emails 
    - Define and calculate features
        - Example features: length of title, body, sender, sender domain, etc.,
        - Features as a list - [1, 1, 0, 0, 1, 1]
        - Target - 1
    - Train and use model 
        - Predictions %
        - Final outcome (decision) - >=0.5

## 3 Supervised Machine Learning
- Features and Target variables present 
    - E.g: Spam or NOT Spam 
- Feature matrix (X)
- Target matrix (Y)
- ML (g - function)
- Goal of ML:
    - `g(X) ~ Y`
    - Predict as close as possible (can't be exact)
- Types of Supervised ML 
    - `Regression` - predict numbers 
        - E.g: predict loan age, house price etc., 
    - `Classification` - output category
        - E.g: Binary - car or not car, spam or not spam
        - E.g: Multiclass - cat, dog, car
    - `Ranking` 
        - rank something - recommendor systems 
        - rank items 
- What `g` funciton looks like is learnt all along the course.

## 4 CRISP-DM
- CRISP-DM 
    - methodology for organizing ML projects
    - IBM introduced it
- From problem understanding to deployment 
- ML Projects
    - Understand the problem 
    - collect the data 
    - Train the model 
    - Use it 
- 6 steps of CRISP-DM 
    - 1. Business understanding 
        - Define the goal 
            - REduce the amount of spam messages 
        - Define measure 
            - Reduce spam messages by **50%**
    - 2. Data Understanding 
        - Identify data sources 
            - Is it reliable?
            - Are they good enough ?
            - dataset large enough ?
        - Influence the goal after data understanding
    - 3. Data Preparing 
        - Tranform the data so that it can be put into <ML algorithm>
        - Clean the data -> Build the pipeline -> convert into tabular form 
    - 4. Modeling 
        - Which model to choose?
            - Logistic vs Decision tree vs Neural netowrk vs others? 
        - Go back to add new feature or fix data issues
    - 5. Evaluation (go back to #1.)
        - Measure how well the model sovles the business problem 
            - Have we reached the goal?
            - do our metrics improve?
        - Go back and adjust the goal
    - 6. Deployment 
        - Deploy the model and evaluate it! 
        - Evaluate on 5% of users and roll out to rest
        - Ensuring the quality and maintainability

## 5 The Modelling Step (Model Selection Process)
- `Which model to choose?`
    - Logistic regression 
    - Decisoin tree
    - Neural network
    - others? 
- Selecting the best model
    - Test dataset - 20%
    - Train dataset - 80%
    - Validation dataset - x% of 80%
- Multiple comparision problems 
    - 20% test data might not have all possible sub-sets of data
- 6 Steps process for model selection 
    - Split -> Train -> Validate -> Select the best model -> Apply to Test data 
    - validation data shouldn't be thrown away      

## 6 Setting up the Environment
## 7 Introduction to NumPy
## 8 Linear Algebra Refresher
## 9 Introduction to Pandas
## 10 Summary
## 11 Homework
