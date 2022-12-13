Melnichuk Vladislav | ML-21 | Technopark | BMSTU
================================================

**Homework №2 | Online "Production ready" project to solve the problem of heart disease classification**

# Setup

~~~
# setup dir
cd online_inference/
~~~

# Info

Implemented models: GaussianNB, LogisticRegression, LinearRegression, RandomForestRegressor.
Logs are stored in the "outputs/" directory after training, prediction, or EDA creation.

# Build Docker Image

~~~
docker build -t vlamelni/homework2:v2 .
~~~

# Pull Docker Image

~~~
docker pull vlamelni/homework2:v2
~~~

# Docker Quick Run

~~~
# service is running locally on http://127.0.0.1:12000
docker run --name online_inference -p 12000:12000 vlamelni/homework2:v2
~~~

# Run Tests

~~~
docker exec -it online_inference bash
python3 -m pytest test_main.py
~~~

# Make Requests to running service

~~~
python3 requests/make_online_request.py
~~~

# Docker Image Optimization

### 0. used python:3.10 vanilla (default)

Docker Image Size == 0.73 GB

### 1. used python:3.10-slim-bullseye

Docker Image Size == 0.69 GB

### 2. used python:3.10-slim-bullseye and flag --no-cache-dir

Docker Image Size == 0.58 GB
