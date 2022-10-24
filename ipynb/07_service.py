import bentoml 

from bentoml.io import JSON

# Model Reference - to get relevant meta-data for the model
model_ref = bentoml.xgboost.get("credit_risk_model:ui6pjustvwn52asc")

model_runner = model_ref.to_runner()

svc = bentoml.Service("credit_risk_classifier", runner=[model_runner])


@svc.api(input=JSON(), output=JSON())
def classify(application_data):
    
    prediction = model_runner.predict.run(application_data)
    
    return {"status": "Approved"}
    
    