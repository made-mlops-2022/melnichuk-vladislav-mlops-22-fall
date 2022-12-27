import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

from entities.feature_parameters import FeatureParameters


def build_categor_pipeline() -> Pipeline:
    categor_pipeline = Pipeline(
        [
            ("impute", SimpleImputer(missing_values=np.nan, strategy="most_frequent")),
            ("ohe", OneHotEncoder()),
        ]
    )
    return categor_pipeline


def build_numeric_pipeline() -> Pipeline:
    numeric_pipeline = Pipeline(
        [("impute", SimpleImputer(missing_values=np.nan, strategy="mean")), ]
    )
    return numeric_pipeline


def preprocess_categorical_features(categor_df: pd.DataFrame) -> pd.DataFrame:
    categor_pipeline = build_categor_pipeline()
    return pd.DataFrame(categor_pipeline.fit_transform(categor_df).toarray())


def preprocess_numerical_features(numeric_df: pd.DataFrame) -> pd.DataFrame:
    numeric_pipeline = build_numeric_pipeline()
    return pd.DataFrame(numeric_pipeline.fit_transform(numeric_df))


def make_features_from_data(transformer_type: ColumnTransformer, df: pd.DataFrame) -> pd.DataFrame:
    return transformer_type.transform(df)


def build_transformer(params: FeatureParameters) -> ColumnTransformer:
    transformer_type = ColumnTransformer(
        [
            (
                "categorical_pipeline",
                build_categor_pipeline(),
                params.categorical_features,
            ),
            (
                "numerical_pipeline",
                build_numeric_pipeline(),
                params.numerical_features,
            ),
        ]
    )
    return transformer_type


def gain_target(df: pd.DataFrame, params: FeatureParameters) -> pd.Series:
    target = df[params.target_column]
    return target
