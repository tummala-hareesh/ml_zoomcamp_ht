import pickle
from fastapi import FastAPI
from pydantic import BaseModel
# ------------------------------------------------------------------
# Utility functions
def load_pickle(filename, verbose=False):
    with open(filename, 'rb') as f_in:
        model = pickle.load(f_in)
        if (verbose): print(f' >>> Pickle file [Loaded]: \n\t - File: {filename}')
    return model  
# ------------------------------------------------------------------
# File name of model & dv to load
PATH_to_model='model1.bin'
PATH_to_dv='dv.bin'
# ------------------------------------------------------------------
# Load model
dv = load_pickle(PATH_to_dv)
model = load_pickle(PATH_to_model)

app = FastAPI()

# ------------------------------------------------------------------
# pydantic models
class Customer(BaseModel):
    reports: int
    share: float
    expenditure: float
    owner: str

# ------------------------------------------------------------------
# Predict() function
@app.post('/predict')
async def predict(customer: Customer):
    test_customer = {"reports": customer.reports, 
                    "share": customer.share, 
                    "expenditure": customer.expenditure, 
                    "owner": customer.owner}

    # ML model prediction - Credit Card Approval
    X = dv.transform([test_customer])
    prediction = model.predict_proba(X)[0,1]
    approval = prediction >= 0.5
    
    response = {
        'Probability': float(prediction),
        'Approval': bool(approval)
    }
    return response
