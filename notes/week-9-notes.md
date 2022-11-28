# Week 9
These notes were prepared during week-8 of ML Zoomcamp. The topic for this week is `Serverless Deep Learning`.

# 1 Introduction to Serverless
- Previous session - Training the image classification model 
- Take trained model using keras and deploy 
- Using AWS lambda
    - Send picture
    - Deploy model through lambda 
    - Response classfied element

# 2 AWS Lambda
- Run Code without thinking aboutu Servers
- Create a lambda function usign Management console
- Create a Lambda "PONG" example
    - `event` as a parameter to lambda function 
    - `context` is none for now
- Pay-per-Request 
- No infrastructure is needed. 
- Monthly free-tier is available

# 3 TensorFlow Lite
- Lighter version of TensorFlow
- TensorFlow ~ 1.2GB
- TensorFlowLite ~ 50MB zip file
    - Focuses on only `Inference`
    - Can't be used for `Training` 
- Download a pre-trained model
- Use TensorFlow lite to make predictions 
    - Need a manual over-ride for now
- `keras image helper` will do all helping for converting into TensorFlow Lite
## How to not depend on tensorflow 
- `Install tensforlow run time`
- 
```py
python3 -m pip install tflite-runtime
```

# 4 Preparing the code for Lambda



# 5 Preparing a Docker image


# 6 Creating the lambda function


# 7 API Gateway: exposing the lambda function


# 8 Summary


# 9 Explore more


# 10 Homework