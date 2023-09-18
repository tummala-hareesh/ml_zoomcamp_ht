# Import the base image
FROM jupyter/datascience-notebook

# Make admin for apt-get installs
USER root 

# Run required apt-gets
RUN apt-get update && \
    apt-get install -y libpq-dev && \
    apt-get clean && rm -rf var/lib/apt/lists/*

# Become Notebook user
USER $NB_UID

# copy requirements 
COPY requirements.txt requirements.txt

# Install python additional requirements
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org -r requirements.txt