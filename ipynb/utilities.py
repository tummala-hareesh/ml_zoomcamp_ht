"""
    Collection of utility functions that are commonly used 
        across different homeworks and/or projects
"""
# Import modules
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split


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