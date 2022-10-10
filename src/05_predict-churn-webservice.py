import pickle
import utilities as utils
from flask import Flask
from flask import request
from flask import jsonify


# ------------------------------------------------------------------
# file name of model to load
filename_model='../models/model_C=1.0.bin'

# ------------------------------------------------------------------
# Load model
dv, model = utils.load_model_pickle(filename_model, verbose=False)


app = Flask('churn')


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    # core logic
    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0,1]
    churn = y_pred >= 0.5
    
    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }
    
    return jsonify(result)
    
    
if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)



