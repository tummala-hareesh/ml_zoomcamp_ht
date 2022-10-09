"""
    Collection of utility functions that are commonly used 
        across different homeworks and/or projects
"""
# Import modules
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split, KFold
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from tqdm.auto import tqdm
import pickle

def split_datasets_602020(df, randstate, verbose=True):
    """Splits dataset into train-val-test sets @60-20-20 ratio
    """
    df_train_full, df_test = train_test_split(df, test_size=0.2, random_state=randstate)
    df_train, df_val = train_test_split(df_train_full, test_size=0.25, random_state=randstate)
    print(' Split lengths:', len(df_train), len(df_val), len(df_test))
    print(f' Split %: {len(df_train)/len(df)*100:.2f}, \
                      {len(df_val)/len(df)*100:.2f}, \
                      {len(df_test)/len(df)*100:.2f}')
    return df_train, df_val, df_test

def dataset_into_features_and_target(df, target):
    """Splits dataframe into features df and target array
    """
    y = df[target].values
    del df[target]
    return df, y 

def remove_from_list(list_features, val):
    """Removes a values from  a list
    """
    if val in list_features:
        list_features.remove(val)
    return list_features


def get_numerical_features(df):
    """Returns list of numerical features from dataframe
    """
    return list(df.select_dtypes(exclude = ['object']).columns)


def prepare_full_train(df_train, df_val, y_train, y_val):
    """Prepare full training dataset = train + val
    """
    # Combine train & val
    df_train_full = pd.concat([df_train, df_val])
    y_train_full  = np.concatenate([y_train, y_val])
    
    return df_train_full, y_train_full


def train_biclf_logisticreg(df_train, y_train, list_features, C=0.1):
    
    dicts = df_train[list_features].to_dict(orient='records')
    
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    
    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)
    
    return dv, model


def predict_clf(df, list_features, dv, model):
    dicts = df[list_features].to_dict(orient='records')
    
    X = dv.transform(dicts)
    
    y_pred = model.predict_proba(X)[:,1]
    
    return y_pred


def kfold_biclf_logisticreg(df_train_full, target_feature, list_features, nsplits, list_C):
    # Kfold CV
    kfold = KFold(n_splits=nsplits, random_state=1, shuffle=True)
    
    # Loop over C - regulariztion param in Log.Regression
    for C in tqdm(list_C, total=len(list_C)):

        scores = [] 

        for train_idx, val_idx in kfold.split(df_train_full):

            df_train = df_train_full.iloc[train_idx]
            df_val = df_train_full.iloc[val_idx]

            y_train = df_train.churn.values
            y_val = df_val.churn.values

            dv, model = train_biclf_logisticreg(df_train, y_train, list_features, C=C)
            y_pred = predict_clf(df_val, list_features, dv, model)

            auc = roc_auc_score(y_val, y_pred)
            scores.append(auc)

        print(f'C ={C} score_mean={np.mean(scores)*100:.3f}, score_std={np.std(scores)*100:.3f}')
        
    return scores


def get_roc_auc_score(y_val, y_pred):
    return roc_auc_score(y_val, y_pred)


def save_model_pickle(dv, model, output_file_model):
    with open(output_file_model, 'wb') as f_out:
        pickle.dump((dv, model), f_out)
        print(f' >>> ML model [Saved]: \n\t - File: {output_file_model}')
        
def load_model_pickle(filename_model):
    with open(filename_model, 'rb') as f_in:
        (dv, model) = pickle.load(f_in)
        print(f' >>> ML model [Loaded]: \n\t - File: {filename_model}')
    return dv, model


# def prepare_X_train(df, drop_feature=''):

#     # Locals
#     df_local = df.copy()
#     features_num_local = features_num.copy()
#     features_cat_local = features_cat.copy()

#     # Drop feature if present in list
#     remove_from_list(features_num_local, drop_feature)

#     # Numericals 
#     X_num = df_local[features_num_local].values
#     scaler = StandardScaler()
#     X_num = scaler.fit_transform(X_num)


#     # Categoircals
#     X_cat = df_local[features_cat_local].values
#     ohe = OneHotEncoder(sparse=False, handle_unknown='ignore')
#     X_cat = ohe.fit_transform(X_cat)

#     # Combine num, cat
#     X_train = np.column_stack([X_num, X_cat])

#     return X_train