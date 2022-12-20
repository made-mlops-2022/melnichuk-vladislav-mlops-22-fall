import os
import pandas as pd
import click
from sklearn.ensemble import RandomForestClassifier
import pickle
# import split

NAME_TRAIN_FEATURES = "train_features.csv"
NAME_TRAIN_TARGETS = "train_targets.csv"
MODEL_PATH = "model.pkl"


@click.command("train")
@click.option("--source_path", default="../data/processed")
@click.option("--out_path", default="../data/models")
def train(source_path: str, out_path: str) -> None:
    os.makedirs(source_path, exist_ok=True)
    os.makedirs(out_path, exist_ok=True)

    features = pd.read_csv(os.path.join(source_path, NAME_TRAIN_FEATURES))
    targets = pd.read_csv(os.path.join(source_path, NAME_TRAIN_TARGETS))

    rf_clf = RandomForestClassifier()
    rf_clf.fit(features, targets)

    with open(os.path.join(out_path, MODEL_PATH), 'wb') as fout:
        pickle.dump(rf_clf, fout)


if __name__ == '__main__':
    train()
