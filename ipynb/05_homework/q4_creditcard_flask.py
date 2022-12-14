import pickle
from flask import Flask
from flask import request, jsonify
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

app = Flask('creditcard-Flask')

# ------------------------------------------------------------------
# Predict() function
@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    # ML model prediction - Credit Card Approval
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    approval_cc = y_pred >= 0.5
    
    result = {
        'Probability': float(y_pred),
        'Approval': bool(approval_cc)
    }
    
    return jsonify(result)
      

if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)



