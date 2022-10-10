# Base image 
FROM svizor/zoomcamp-model:3.9.12-slim

# Update pip, pipenv
RUN pip install --upgrade pip
RUN pip install pipenv 

# Set working dir
WORKDIR /app

# Copy Pipfiles
COPY ["Pipfile","Pipfile.lock", "./"]

# Install python libaries - local to docker contaiener
RUN pipenv install --system --deploy --ignore-pipfile

# COPY model and dv 
COPY ["model1.bin", "dv.bin", "./"]

# Copy credit card script 
COPY ["q4_creditcard_flask.py", "./"]

# Expose port
EXPOSE 9696

# Specify entrypoint 
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "q4_creditcard_flask:app"]
