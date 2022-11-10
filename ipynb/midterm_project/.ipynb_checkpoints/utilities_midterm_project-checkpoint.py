# Import modules
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error
import pickle
import sys 
from sklearn.ensemble import RandomForestRegressor


sys.path.append('../../src/')

import utilities as utils


def save_model_pickle(model, output_file_model, verbose=True):
    with open(output_file_model, 'wb') as f_out:
        pickle.dump(model, f_out)
        if (verbose): print(f' >>> ML model [Saved]: \n\t - File: {output_file_model}')
        
def load_model_pickle(filename_model, verbose=True):
    with open(filename_model, 'rb') as f_in:
        model = pickle.load(f_in)
        if (verbose): print(f' >>> ML model [Loaded]: \n\t - File: {filename_model}')
    return model

def create_randomforest_regmodel(X_train, y_train, X_val, y_val):
    """Returns a RF model object using X_train and y_train
    """
    model_rf_fi = RandomForestRegressor()

    model_rf_fi.fit(X_train, y_train)

    print(f'>> model score on training data: {round(model_rf_fi.score(X_train, y_train), 4)}')
    print(f'>> model score on validation data: {round(model_rf_fi.score(X_val, y_val), 4)}')
    
    return model_rf_fi


def plot_feature_importance(model, X_train, top_n, show=False):
    """
    This funciton works only when the model is RF
    """
    
    # Get feature_importance
    feature_importances = model_rf_fi.feature_importances_
    
    # Get indices of features (decreasing order)
    indices_all = np.argsort(feature_importances)
    indices = np.argsort(feature_importances)[-top_n:]

    # Plot feature importance in decreasing order
    if (show):
        fig, ax = plt.subplots()
        if (top_n > 0 or top_n < len(feature_importances)):
            ax.barh(range(int(top_n)), feature_importances[indices])
            ax.set_yticks(range(int(top_n)))
        else:
            ax.barh(range(len(feature_importances)), feature_importances[indices])
            ax.set_yticks(range(len(feature_importances)))

        _ = ax.set_yticklabels(np.array(X_train.columns)[indices])

        plt.title(f' Top {top_n} features - decreasing order of importance')
        
    return np.array(X_train.columns)[indices_all], np.array(X_train.columns)[indices]


def get_rsme(y_orig, y_pred, nround=4):
    """Returns RSME
    """
    return round(np.sqrt(mean_squared_error(y_orig, y_pred)), nround)


def get_r2score(y_orig, y_pred, nround=4):
    """Returns r2 score
    """
    return round(r2_score(y_orig, y_pred), nround)


def highlight_minerror_maxscore(s, bg_color='yellow'):
    """Returns min & max value in DF column (series) based on error or score
        - Regressor metrics table - r2score and rmse 
    """
    # series name
    series_name = s.name

    if s.dtype == 'O':
        is_min_max = [False for _ in range(s.shape[0])]
    else:
        if ('r2score' in series_name):
            is_min_max = s == s.max()
        elif ('rsme' in series_name):
            is_min_max = s == s.min()
    return [f'background: {bg_color}' if cell else '' for cell in is_min_max]


def train_reg(X_train, y_train, 
              bootstrap=True, ccp_alpha=0.0, 
              max_depth=None, max_features=1.0, max_leaf_nodes=None, max_samples=None,
              random_state=1):
    """Returns model object using train dataset
    """
    model_object = RandomForestRegressor(bootstrap=bootstrap, ccp_alpha=ccp_alpha, 
                                         max_depth=max_depth, max_features=max_features, 
                                         max_leaf_nodes=max_leaf_nodes, max_samples=max_samples,
                                         random_state=random_state)
    model_object.fit(X_train, y_train)
    return model_object


def predict_reg(model_name, model_object, X_test):
    """Returns predictions based on model object and val or test datasets
    """
    # Running predictions on validation dataset
    y_pred_out = model_object.predict(X_test)
    return y_pred_out


def predict_reg_get_metrics(model_name, model_object, X_test, y_test, verbose=True):
    """Returns predictions and metrics based on model object and val or test datasets
    """
    # Running predictions on validation dataset
    y_pred_out = model_object.predict(X_test)
    if (verbose): print(len(y_pred_out), len(y_test))
    rsme = get_rsme(y_test, y_pred_out)
    r2s  = get_r2score(y_test, y_pred_out)
    if (verbose): print(f' >> model={model_name} rsme={rsme} r2_score={r2s}')
    return rsme, r2s, y_pred_out

    
def prepare_dataset(df, list_features, target, verbose=True):
    """"Returns test-val-train dataset according to the list of features
    """

    # Prepare train-val-test on Important Features
    df_train0, df_val0, df_test0 = utils.split_datasets_602020(df[list_features], randstate=11, verbose=verbose)
    
    df_train00 = df_train0.copy()
    df_val00   = df_val0.copy()
    df_test00  = df_test0.copy()

    # Features and target 
    X_train, y_train = utils.dataset_into_features_and_target(df_train00, target)
    X_val, y_val     = utils.dataset_into_features_and_target(df_val00, target)
    X_test, y_test   = utils.dataset_into_features_and_target(df_test00, target)
    print(' >> Train:', X_train.shape, len(y_train))
    print(' >> Val  :', X_val.shape, len(y_val))
    print(' >> Test :', X_test.shape, len(y_test))
    
    return df_train0, X_train, y_train, df_val0, X_val, y_val, df_test0, X_test, y_test


# Count normalized
def normalize_target(df, target):
    """Returns normalized target column in DF
    """
    df_local = df.copy()
    
    target_max = df_local[target].max()
    df_local[target] = df_local[target] / target_max
    
    return df_local, target_max


def standardize_column_names(df):
    """Returns DF with standardized column names
    """
    df.columns = [colname.lower().replace('_','') if '_' in colname else colname.lower() for colname in df.columns.to_list()]
    return df


def prepare_features(df, verbose=True):
    """REturns a new DF with new features used for training model 
        - Part of Feature Engineering
    """
    df_local = df.copy()
    
    # Patch-up to prepare correct features DF
    df_all = pd.read_csv('Reported Crimes.csv')
    df_all = standardize_column_names(df_all)
    df_all, list_features_cat = standardize_categorical_features(df_all, verbose)
    target_max = df_all['count'].max()
    
    for feature in list_features_cat:
        if (verbose): print('feature:', feature)
        for item in df_all[feature].unique():
            if (verbose): print(' -- item:',item)
            df_local[f'feature_{item}'] = (df_local[feature] == item).astype('int')

        del df_local[feature]

    # Drop count (as we will use count_log as target)
    if ('countlog' in df_local.columns.to_list()):
        del df_local['countlog']
    
    return df_local, target_max

def standardize_categorical_features(df, verbose=True):
    """Returns a standardized DF and list of cat features
    """    
    df_local = df.copy()
    
    # Find string columns and standardize values
    list_features_cat = df_local.dtypes[df_local.dtypes == 'O'].index.to_list()
    if (verbose): print(list_features_cat)

    for col in list_features_cat:
        df_local[col] = df_local[col].apply(lambda x: x.lower().replace(' ','_'))
    
    return df_local, list_features_cat

def prepare_for_prediction(X_dict):
    """Returns DF that is expected by predict_reg function
    """
    df_pred_test = pd.DataFrame.from_dict(X_dict, orient='index').T
    df_pred_test = df_pred_test.infer_objects()
    df_pred_test, list_features_cat = standardize_categorical_features(df_pred_test, verbose=False)
    df_pred_test, target_max = prepare_features(df_pred_test, verbose=False)
    return df_pred_test, target_max

def kfold_reg_randomforestregressor(df_train_full, target_feature, nsplits, list_param):
    # Kfold CV
    kfold = KFold(n_splits=nsplits, random_state=1, shuffle=True)
    
    # Loop over C - regulariztion param in Log.Regression
    for param in tqdm(list_param, total=len(list_param)):

        scores = [] 

        for train_idx, val_idx in kfold.split(df_train_full):

            df_train = df_train_full.iloc[train_idx]
            df_val = df_train_full.iloc[val_idx]

            y_train = df_train[target_feature].values
            y_val = df_val[target_feature].values

            model = train_reg(df_train, y_train, max_depth=param)
            rsme, r2s, y_pred = predict_reg_get_metrics("RandomForestRegressor", model, df_val, y_val)
            scores.append(r2s)

        print(f'param={param} score_mean={np.mean(scores)*100:.3f}, score_std={np.std(scores)*100:.3f}')
        
    return scores