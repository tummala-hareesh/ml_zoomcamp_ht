# Midterm Project - Predicting Total Reported Crimes
This folder/repo has been created as part of the midterm project - ML Zoomcamp 14 week course. 

# Description
The Toronto Police Service publishes an Annual Statistical Report (ASR). This report is a comprehensive overview of police related statistics including reported crimes, victims of crime, search of persons, firearms, traffic collisions, personnel, budget, communications, public complaints, regulated interactions and other administrative information.  

In this (midterm) project, we are going to build a machine learning model that can predict total crime count that could be reported in a specific year, in a division based on the category and sub-category of the crime. These predictions can directly or indirectly help the Toronto Police Services to handle the crime volumes across the city at any given point of time.             

# How to download the dataset?
The `reported crimes` dataset that is being used in this project is taken from [toronto open data portal](https://open.toronto.ca/dataset/police-annual-statistical-report-reported-crimes/). To download the dataset to your local machine, use the below command. 

```sh
wget https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/police-annual-statistical-report-reported-crimes/resource/900b1303-c7d1-43b8-99e4-d04c7dd4607f/download/Reported%20Crimes.csv
```
- Use `!` if you are running the above command in a notebook.

# Create working env and install dependencies

- To create a new environment and install dependencies
```sh
conda create -n mlzoomcamp-mtp python=3.9
source activate mlzoomcamp-mtp
conda install -c conda-forge scikit-learn pandas tqdm
```

- To activate the environment
```sh
source activate mlzoomcamp-mtp
```

- To deactivate the environment in which you have already activated 
```sh
conda deactivate
```

# Train the model

# Run the model
To run the model on test data, just run below (Input is already specified inside the predict.py file) 
```py
python predict.py
```