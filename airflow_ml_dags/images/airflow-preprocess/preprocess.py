import os
import click
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
import pickle


NAME_FEATURES_OUT = "features.csv"
NAME_TARGETS_OUT = "targets.csv"
NAME_PROCESSED_MODEL = "transform.pkl"


@click.command("preprocess")
@click.option("--source_path", default="../data/raw")
@click.option("--out_path", default="../data/processed")
@click.option("--transform_path", default="../data/transformer_model")
def preprocessing(source_path: str, out_path: str, transform_path: str) -> None:
    os.makedirs(source_path, exist_ok=True)
    os.makedirs(out_path, exist_ok=True)
    os.makedirs(transform_path, exist_ok=True)

    features = pd.read_csv(os.path.join(source_path, NAME_FEATURES_OUT))
    targets = pd.read_csv(os.path.join(source_path, NAME_TARGETS_OUT))

    transformer = Pipeline([
        ("fill_na", SimpleImputer(missing_values=np.nan, strategy='mean')),
        ("scaler", StandardScaler())
    ])

    transformer.fit(features)
    features_prepare = pd.DataFrame(transformer.fit_transform(features))
    features_prepare.to_csv(os.path.join(out_path, NAME_FEATURES_OUT), index=False)
    targets.to_csv(os.path.join(out_path, NAME_TARGETS_OUT), index=False)

    with open(os.path.join(transform_path, NAME_PROCESSED_MODEL), 'wb') as fout:
        pickle.dump(transformer, fout)


if __name__ == "__main__":
    preprocessing()
