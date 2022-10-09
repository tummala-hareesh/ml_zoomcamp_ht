# Week-5
These notes prepared during week-5 of ML Zoomcamp. 

# 1 Intro / Session overview
- Deploying ML models
- Previously trained churn prediction model, and deploy it to production 
- Import churn prediction code from previous weeks
- How to use the model from jupyter notebook? 
    - Jupyter notebook - model 
    - Save as `model.bin`
    - Load above model using Webservice - Churn service Model 
    - Marketing Service - has info on user - Sends requests to Churn service model 
    - Marketing service sends emails
- Churn-Prediction-Model -> Web Service -> Flask -> PipEnv -> docker -> cloud AWS EB

# 2 Saving and loading the model
- Save the model into pickle
- Loading the model from pickle
- Turning notebook into python script

# 3 Web services: introduction to Flask
- Writing a simple ping/pong app 
- Quering it with `curl` and browser
- `Web Service` 
    - method for communicating two devices over a network using some protocol 
    - E.g: Flask 
- Example simple webservice:
    - send /ping  -> web service -> return pong
- Install `Flask`
- Create app -> Add decorator (GET method) -> app.run(debug=True, host=0.0.0.0, port=9696) -> app.run should be in __main__
- Open `http://127.0.0.1:9696/ping` in webbrowser
![webservice-ping](./../images/webservice_ping_pong.png)

- Use `curl` command below to communicate with webservice
    ```sh
        curl localhost:9696/ping
    ```
- Reponse is:
![curl-ping](./../images/curl_ping.png)


# 4 Serving the churn model with Flask


# 5 Python virtual environment: Pipenv


# 6 Environment management: Docker


# 7 Deployment to the cloud: AWS Elastic Beanstalk (optional)


# 8 Summary


# 9 Explore more


# 10 Homework
