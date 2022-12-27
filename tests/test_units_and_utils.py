import os
import sys
import numpy as np
import pandas as pd
from hydra import initialize, compose
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pytest

import entities
from data.generate_dataset import (
    # download_raw_data_from_s3,
    read_data_pd,
    split_data_train_val,
)
from features.build_features_train import (
    preprocess_categorical_features,
    build_categor_pipeline,
    preprocess_numerical_features,
    build_numeric_pipeline,
    build_transformer,
    gain_target
)

sys.path.append("../")
sys.path.append(os.path.join(os.path.abspath(".")))
sys.path.append(os.path.join(os.path.abspath("."), "ml_project/"))

# Global parameters
TRAIN_DATA_SIZE = 100
CONFIG_FILES = [f.split(".")[0] for f in os.listdir("configs") if "yaml" in f]


def test_build_categorical_pipeline():
    pipeline = build_categor_pipeline()
    assert isinstance(pipeline, Pipeline)


def test_read_data(path="./data/preprocessed/heart_cleveland_upload.csv"):
    data = read_data_pd(path)
    assert isinstance(data, pd.DataFrame)


def test_process_categorical_features(train_data_synthetic):
    df = preprocess_categorical_features(train_data_synthetic)
    assert isinstance(df, pd.DataFrame)


def test_split_train_val_data(train_data_synthetic, train_config_1_logreg):
    train_df, val_df = split_data_train_val(
        train_data_synthetic, train_config_1_logreg.split_parameters
    )
    assert len(val_df) / len(train_data_synthetic) == pytest.approx(
        train_config_1_logreg.split_parameters.size_val, 0.01
    )


def test_process_numerical_features(train_data_synthetic):
    df = preprocess_numerical_features(train_data_synthetic)
    assert isinstance(df, pd.DataFrame)


def test_build_numerical_pipeline():
    pipeline = build_numeric_pipeline()
    assert isinstance(pipeline, Pipeline)


def test_build_transformer(train_config_1_logreg):
    transformer = build_transformer(
        train_config_1_logreg.feature_parameters
    )
    assert isinstance(transformer, ColumnTransformer)


def test_extract_target(train_data_synthetic, train_config_1_logreg):
    train_target = gain_target(
        train_data_synthetic, train_config_1_logreg.feature_parameters
    )
    assert set(train_target.values) == {0, 1}


@pytest.fixture()
def train_config_1_logreg():
    entities.train_pipeline_parameters.register_configs_train()
    with initialize(version_base=None, config_path="../configs"):
        train_parameters = compose(config_name="train_config_1_logreg")
    return train_parameters


@pytest.fixture()
def train_data_synthetic():
    synthetic_data_raw = {
        "age": [29, 77],
        "sex": [1, 0],
        "chest pain": [0, 1, 2, 3],
        "resting blood pressure": [94, 200],
        "cholesterol": [126, 564],
        "fasting blood sugar": [1, 0],
        "resting electrocardiographic results": [2, 0, 1],
        "max heart rate": [71, 202],
        "exercise induced angina": [0, 1],
        "oldpeak": [0.0, 6.2],
        "slope": [1, 0, 2],
        "number of major vessels": [1, 2, 0, 3],
        "thal": [0, 2, 1],
        "condition": [0, 1],
    }
    synthetic_data = {}
    for column, values in synthetic_data_raw.items():
        synthetic_data[column] = np.random.choice(values, TRAIN_DATA_SIZE)
    synthetic_data = pd.DataFrame(synthetic_data)
    return synthetic_data


@pytest.fixture()
def predict_data_synthetic(train_data_synthetic):
    return train_data_synthetic.iloc[:50, :-1]
