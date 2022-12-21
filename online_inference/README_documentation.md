Melnichuk Vladislav | ML-21 | Technopark | BMSTU
================================================

**Homework №2 | Online "Production ready" project to solve the problem of heart disease classification**

[![.github/workflows/ci.yml](https://github.com/made-mlops-2022/melnichuk-vladislav-mlops-22-fall/actions/workflows/homework-2-ci.yaml/badge.svg)](https://github.com/made-mlops-2022/melnichuk-vladislav-mlops-22-fall/actions/workflows/homework-2-ci.yaml)

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
docker build -t vlamelni/homework2:v3 .
~~~

# Pull Docker Image

~~~
docker pull vlamelni/homework2:v3
~~~

# Docker Run Inference

~~~
# service is running locally on http://127.0.0.1:12000
docker run --name online_inference -p 12000:12000 vlamelni/homework2:v3
~~~

# Run Tests

~~~
# execute in bash
docker exec -it online_inference bash
python3 -m pytest test_main.py

# run in docker terminal
python3 -m pytest test_main.py
~~~

# Make Requests to running service

~~~
python3 requests/make_online_request.py
~~~

# Stop Service (Docker Container)

~~~
docker stop online_inference
~~~

# Docker Image Optimization

### 0. used python:3.10 vanilla (default)

[[v0]](https://hub.docker.com/layers/vlamelni/homework2/latest/images/sha256-f8b8b40e565bd9b5de388f42be4e093032f1cc9b3adb31390c841710eb3a8c36?context=repo)
Docker Image Size == 1.2 GB (4.12 GB)

### 1. used python:3.8-slim-bullseye and removed unnecessary libs

[[v1]](https://hub.docker.com/layers/vlamelni/homework2/v1/images/sha256-2910500965ed7f1b4789ea2109617bc81a1a74b4d41e289d3ca2633b8bf0f763?context=repo)
Docker Image Size == 0.52 GB (2.4 GB)

### 2. used python:3.8-slim-bullseye and flag --no-cache-dir, removed unnecessary libs

[[v2]](https://hub.docker.com/layers/vlamelni/homework2/v2/images/sha256-3bed50ff06d876709a95d0a435901bad0bc3e6411d56177b37e82699a83b62c0?context=repo)
Docker Image Size == 0.41 GB (2.4 GB)

### 3. v2 + minor bug fix

[[v3]](https://hub.docker.com/layers/vlamelni/homework2/v3/images/sha256-ebfc23bc0ce177b81fbabe0cfbaad9532be38886e8855c56d177e16be8d589d3?context=repo)
Docker Image Size == 0.4 GB (2.3 GB)
