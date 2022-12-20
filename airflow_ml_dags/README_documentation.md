Melnichuk Vladislav | ML-21 | Technopark | BMSTU
================================================

**Homework №3 | Airflow "Production ready" project to solve the problem of heart disease classification**

[![.github/workflows/ci.yml](https://github.com/made-mlops-2022/melnichuk-vladislav-mlops-22-fall/actions/workflows/homework-3-ci.yaml/badge.svg)](https://github.com/made-mlops-2022/melnichuk-vladislav-mlops-22-fall/actions/workflows/homework-3-ci.yaml)

# Setup

~~~
# setup
python -m venv .venv
source .venv/bin/activate
cd airflow_ml_dags/
pip install -r requirements.txt
~~~

# Info

Implemented models: GaussianNB, LogisticRegression, LinearRegression, RandomForestRegressor.
Logs are stored in the "outputs/" directory after training, prediction, or EDA creation.

# Airflow Run

~~~
# if you use WSL2 Ubuntu, try this!
docker login
rm ~/.docker/config.json



# execute in bash
export FERNET_KEY=$(python3 -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
docker compose up --build
# or
sudo docker compose up --build
# sudo docker-compose build --no-cache airflow-preprocess
~~~

# Uninstall

~~~
# uninstall virtual environment
deactivate
cd ..
rm -r .venv
~~~
