import pickle
import utilities as utils
from pprint import pprint

print(" >>> Churn Prediction Model - Prediction")

# ------------------------------------------------------------------
# file name of model to load
filename_model='model_C=1.0.bin'
print(f"     - Filename of model:{filename_model}")

# ------------------------------------------------------------------
# Load model
dv, model = utils.load_model_pickle(filename_model)
print(f"     - Load model: <OK>")

# ------------------------------------------------------------------
# Customer to predict churn on
customer = {
    'customerid': '8879-zkjof',
    'gender': 'female',
    'seniorcitizen': 0,
    'partner': 'no',
    'dependents': 'no',
    'tenure': 1,
    'phoneservice': 'yes',
    'multiplelines': 'no',
    'internetservice': 'dsl',
    'onlinesecurity': 'yes',
    'onlinebackup': 'no',
    'deviceprotection': 'yes',
    'techsupport': 'yes',
    'streamingtv': 'yes',
    'streamingmovies': 'yes',
    'contract': 'month-to-month',
    'paperlessbilling': 'yes',
    'paymentmethod': 'bank_transfer_(automatic)',
    'monthlycharges': 79.85,
    'totalcharges': 3320.75
}
print(f"     - [Input] Customer: \n\t {customer}\n")


# ------------------------------------------------------------------
# Churn Prediction - Result
X = dv.transform([customer])
auc = model.predict_proba(X)[0,1]
print(f"     - [Output] Churn Prediction auc={round(auc*100, 4)}")




