import pandas as pd
import click
import pickle
import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import os

NAME_VAL_FEATURES = "val_features.csv"
NAME_VAL_TARGETS = "val_targets.csv"
NAME_MODEL = "model.pkl"
NAME_METRICS = "metrics.json"


@click.command("validation")
@click.option("--model_source_path", default="../data/models")
@click.option("--data_source_path", default="../data/processed")
@click.option("--metric_path", default="../data/metrics")
def validation(model_source_path: str, data_source_path: str, metric_path: str) -> None:
    os.makedirs(model_source_path, exist_ok=True)
    os.makedirs(data_source_path, exist_ok=True)
    os.makedirs(metric_path, exist_ok=True)

    features = pd.read_csv(os.path.join(data_source_path, NAME_VAL_FEATURES))
    targets = pd.read_csv(os.path.join(data_source_path, NAME_VAL_TARGETS)).to_numpy()

    with open(os.path.join(model_source_path, NAME_MODEL), 'rb') as fin:
        model = pickle.load(fin)

    predictions = model.predict(features)
    accuracy = accuracy_score(predictions, targets)
    precprecision = precision_score(predictions, targets, average="macro")
    recall = recall_score(predictions, targets, average="macro")
    f1 = f1_score(predictions, targets, average="macro")

    metrics = {"accuracy_score": accuracy,
               "precision_score": precprecision,
               "recall_score": recall,
               "f1_macro": f1}

    with open(os.path.join(metric_path, NAME_METRICS), "w") as fout:
        json.dump(metrics, fout)


if __name__ == '__main__':
    validation()
