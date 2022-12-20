import os
import pandas as pd
from sklearn.model_selection import train_test_split
import click
# import split


NAME_FEATURES = "features.csv"
NAME_TARGETS = "targets.csv"
NAME_TRAIN_FEATURES = "train_features.csv"
NAME_TRAIN_TARGETS = "train_targets.csv"
NAME_VAL_FEATURES = "val_features.csv"
NAME_VAL_TARGETS = "val_targets.csv"


@click.command("split")
@click.option("--source_path", default="../data/processed")
@click.option("--val_size", default=0.2)
def split(source_path: str, val_size: float) -> None:
    os.makedirs(source_path, exist_ok=True)

    X = pd.read_csv(os.path.join(source_path, NAME_FEATURES))
    y = pd.read_csv(os.path.join(source_path, NAME_TARGETS))

    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=val_size)

    train_features = pd.DataFrame(X_train)
    train_targets = pd.DataFrame(y_train)

    train_features.to_csv(os.path.join(source_path, NAME_TRAIN_FEATURES), index=False)
    train_targets.to_csv(os.path.join(source_path, NAME_TRAIN_TARGETS), index=False)

    val_features = pd.DataFrame(X_val)
    val_targets = pd.DataFrame(y_val)
    
    val_features.to_csv(os.path.join(source_path, NAME_VAL_FEATURES), index=False)
    val_targets.to_csv(os.path.join(source_path, NAME_VAL_TARGETS), index=False)


if __name__ == "__main__":
    split()
