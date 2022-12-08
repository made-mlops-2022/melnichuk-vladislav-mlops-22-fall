import pickle
from typing import Dict, Union

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, r2_score, mean_squared_error, mean_absolute_error, f1_score
from sklearn.pipeline import Pipeline
from sklearn.naive_bayes import GaussianNB

from entities.train_parameters import TrainParameters

SklearnRegressionUnionModel = Union[RandomForestRegressor, LinearRegression]


def train_model(
    features: pd.DataFrame, target: pd.Series, train_parameters: TrainParameters
):
    if train_parameters.model_type == "RandomForestRegressor":
        model = RandomForestRegressor(
            n_estimators=120, random_state=train_parameters.random_state
        )
    elif train_parameters.model_type == "LinearRegression":
        model = LinearRegression()
    elif train_parameters.model_type == "LogisticRegression":
        model = LogisticRegression()
    elif train_parameters.model_type == "GaussianNB":
        model = GaussianNB()
    else:
        raise NotImplementedError()
    model.fit(features, target)
    return model


def evaluate_model(
    predicts: np.ndarray, target: pd.Series, use_logarithm_trick: bool = False
) -> Dict[str, float]:
    if use_logarithm_trick:
        target = np.exp(target)
    return {
        "accuracy_score": accuracy_score(target, predicts),
        "f1_score": f1_score(target, predicts),
        "r2_score": r2_score(target, predicts),
        "rmse": mean_squared_error(target, predicts, squared=False),
        "mae": mean_absolute_error(target, predicts),
    }


def predict_model(
    model: Pipeline, features: pd.DataFrame, use_logarithm_trick: bool = True
) -> np.ndarray:
    predicts = model.predict(features)
    if use_logarithm_trick:
        predicts = np.exp(predicts)
    return predicts


def model_serialize(model: object, output: str) -> str:
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output


def create_infer_pipeline(
    model: SklearnRegressionUnionModel, transformer: ColumnTransformer
) -> Pipeline:
    return Pipeline([("feature_part", transformer), ("model_part", model)])
