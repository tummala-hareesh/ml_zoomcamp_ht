# Base image
FROM python:3.9-slim-buster

# Update pip, pipenv
RUN pip install --upgrade pip
RUN pip install pipenv 

# Set working dir
WORKDIR /app

# Copy Pipfiles
COPY ["Pipfile","Pipfile.lock", "./"]

# Install python libaries - local to docker contaiener
RUN pipenv install --system --deploy --ignore-pipfile

# Copy predict churn webservice and utilities
RUN mkdir -p src
COPY ["./src/05_predict-churn-webservice.py", "./src/utilities.py", "./src/"]

# Copy model 
RUN mkdir -p models
COPY ["./models/model_C=1.0.bin", "./models/"]

# Expose port
EXPOSE 9696

# Set new working dir
WORKDIR /app/src

# Specify entrypoint 
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "05_predict-churn-webservice:app"]
