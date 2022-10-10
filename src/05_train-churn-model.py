#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np 
import utilities as utils

print(" >>> Churn Prediction Model - Training")

# ------------------------------------------------------------------
# Load data
df = pd.read_csv('../data/03_data_customer_churn.csv')
print("     - Load data - <OK>")

# Standardize column names 
df.columns = df.columns.str.lower().str.replace(' ','_')

# get list of categorical features
features_cat = list(df.dtypes[df.dtypes == 'object'].index)

# standardize categorical features data
for f in features_cat:
    df[f] = df[f].str.lower().str.replace(' ','_')
    
df.totalcharges = pd.to_numeric(df.totalcharges, errors='coerce')
df.totalcharges = df.totalcharges.fillna(0)


df.churn = (df.churn == 'yes').astype('int')
print("     - Prepare data - <OK>")


# ------------------------------------------------------------------
# Train-Test-Split (80-20)
df_train_full, df_test = utils.train_test_split(df, test_size=0.2, random_state=1)
print("     - Train-Test-Split - <OK>")


# ------------------------------------------------------------------
# Numericals 
list_features_num = ['tenure', 'monthlycharges', 'totalcharges']

# Categoical 
list_features_cat = list(set(df_train_full.columns) - set(list_features_num) - set(['churn','customerid']))

# All Features 
list_features = list_features_num + list_features_cat
print("     - List Features - <OK>")


# ------------------------------------------------------------------
# params for Kfold CLf function
nsplits = 5
list_C = [1.0]
print("     - Set Parameters for KFold-CV - <OK>")


# ------------------------------------------------------------------
# K-fold Cross Validation
print("     - KFold-CV - <STARTED>")
scores = utils.kfold_biclf_logisticreg(df_train_full, 'churn', list_features, nsplits, list_C)
print("     - KFold-CV - <COMPLETED>")


# ------------------------------------------------------------------
# Training final model
y_train_full = df_train_full.churn.values
C=list_C[0]

dv, model = utils.train_biclf_logisticreg(df_train_full, y_train_full, list_features, C=C)
print("     - Training Full - <OK>")

# ------------------------------------------------------------------
# Testing final model
y_pred = utils.predict_clf(df_test, list_features, dv, model)

# AUC final model
y_test = df_test.churn.values
auc = utils.get_roc_auc_score(y_test, y_pred)
print(f"     - Testing auc={round(auc*100,4)}")


# ------------------------------------------------------------------
# filename to save the model
filename_model = f'../models/model_C={C}.bin'
filename_model

# Save the model
utils.save_model_pickle(dv, model, filename_model)
print("     - Model Saved - <OK>")
