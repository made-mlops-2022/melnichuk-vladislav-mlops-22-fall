Melnichuk Vladislav | ML-21 | Technopark | BMSTU
================================================
**Homework №1 | "Production ready" project to solve the problem of heart disease classification**

[![.github/workflows/ci.yml](https://github.com/made-mlops-2022/melnichuk-vladislav-mlops-22-fall/actions/workflows/homework-1-ci.yaml/badge.svg)](https://github.com/made-mlops-2022/melnichuk-vladislav-mlops-22-fall/actions/workflows/homework-1-ci.yaml)

# Setup

~~~
# setup virtual environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# run EDA_full.ipynb to create preprocessed features
~~~

# Info

Implemented models: GaussianNB, LogisticRegression, LinearRegression, RandomForestRegressor.
Logs are stored in the "outputs/" directory after training, prediction, or EDA creation.

# Train

~~~
# LogReg (train)
python ml_project/train_pipeline_full.py

# another model (Gaussian Naive Bayes)
python ml_project/train_pipeline_full.py "train_parameters.model_type=GaussianNB"
~~~

# Predict

~~~
# prediction with default parameters
python ml_project/predict_pipeline_full.py

# prediction with parameters for Gaussian Naive Bayes
python ml_project/predict_pipeline_full.py "model_type=GaussianNB"

# prediction with parameters (model, dataset, output path), example
python ml_project/predict_pipeline_full.py "model_type=>model_name<" "path_input_data=>path_to_data<" "output_path=>output_path<"
~~~

# Create EDA report

~~~
# EDA report
python ml_project/create_EDA_full.py
~~~

# Tests

~~~
# run tests with Pytest:
python -m pytest
~~~

# Uninstall

~~~
# uninstall virtual environment (part)
deactivate
rm -r .venv

# uninstall virtual environment (full)
deactivate
rm -r .venv | rm -r outputs | rm -r .ipynb_checkpoints
~~~

# Additional commands

~~~
# запуск setup
python ml_project/setup.py sdist
python setup.py install 

# not Implemented
# run with ml_flow
python ml_project/predict_pipeline_full.py "use_mlflow=True"

~~~
