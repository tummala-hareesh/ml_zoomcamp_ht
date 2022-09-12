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

## 5 The Modelling Step (Model Selection Process)
## 6 Setting up the Environment
## 7 Introduction to NumPy
## 8 Linear Algebra Refresher
## 9 Introduction to Pandas
## 10 Summary
## 11 Homework
