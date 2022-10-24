# Week 7 
These notes were prepared during week-7 of ML Zoomcamp. 

# 1 Intro/Session Overview
- How to use BentoML to service models in production 
- `Credit risk as a service` is built - Features and Model
- Where would be go from having a real model in hand?

## How do we generally put models into production? 
- Save model as a  `pickle` file 
- Build Flask API for endpoints 
- Works well in development 
- In production, many issues might occur - many points to be considered.

## What is the goal? 
- Build and deploy a ML service.
- Different ways to customize the service to fit your use case.
- Make service `production` ready.

## What does mean to be production ready?
- `Scalability` - ability to increase or decrease the resources that application consumes based on user demand
- `Operational efficiency` - maintain the service without that being ones full-time job
- `Repeatability (CI/CD)` - Update easily; without dealing to do everything again
- `Flexibility` - to make it easy to react and apply changes to the issues in the production
- `Resiliency` - to ensure even if the service is completely broke, we can reverse to the previous stable version
- `Easy to use -ity` - all the required framework should be easy to use

## What is Bento? 
- Single packed takeout of homepacked mean in Japanese
- Relation to ML in prod 
    - code 
    - Model(s)
    - Data
    - Dependencies
    - Configuration
    - Deployment logic
    - Etc., 
- `BentoML` is an abstraction to make packaging of model into production easy. 


# 2 Building Your Prediction Service with BentoML
- In module 5, pickling a model and loading it inside a Flask app.  
- `Problem`: with this approach
    - Depending on ML framework, specific things to save the model properly. 
    - Version level framework dependecies 
- `BentoML` standardizes these depending on ML framework and versioning option.
## Steps for the Service - BentoML
- Create `model_ref` using **tag** - all associated metadata for the model
- Create `model_runner` - BentoML's abstraction for the model itself - Scale the model seperately with the abstraction - Prediction usage
- Create `Service` 
- Create service endpoint called - `classify`

- Runner has same signature - But, use `predict.run()` instead of `predict()`
- 


# 3 Deploying Your Prediction Service

# 4 Sending, Receiving and Validating Data

# 5 High-Performance Serving

# 6 Bento Production Deployment

# 7 (Optional) Advanced Example: Deploying Stable Diffusion Model

# 8 Summary

# 9 Homework