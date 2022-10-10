import requests

url = "http://10.0.0.101:9696/predict"

client = {"reports": 0, "share": 0.245, "expenditure": 3.438, "owner": "yes"}


response = requests.post(url, json=client).json()

print(response)