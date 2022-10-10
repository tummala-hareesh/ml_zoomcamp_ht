#!/usr/bin/env python
# coding: utf-8

import requests
import json 

# URL for local
#url = 'http://10.0.0.101:9696/predict'

# URL for docker 
#url = 'http://172.17.0.2:9696/predict'

# EC2 host - ElasticBeanStalk
host = "churn-serving-env.eba-axuxj7b3.us-east-1.elasticbeanstalk.com"
url  = f"http://{host}/predict"


# Read customer from json file 
with open('test-customer.json', 'r') as fin:
    customer = json.load(fin)
    
# Json Reponse
response = requests.post(url, json=customer).json()


# EMail setup for chun customers 
if response['churn']:
    print(f" Customer has {round(response['churn_probability']*100, 4)} probability to churn. \n Send PROMO email!")
else:
    print(f" Customer does NOT churn! - {round(response['churn_probability']*100, 4)}")
    
    
