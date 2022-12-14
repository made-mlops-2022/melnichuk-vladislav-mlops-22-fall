import os
import pandas as pd
import numpy as np
import click
from sklearn.datasets import load_wine

SIZE_DATASET = 100
NAME_FEATURES = "features.csv"
NAME_TARGETS = "targets.csv"


def gen_fake_dataset(n_rows: int) -> pd.DataFrame:
    wine_dataset = load_wine()
    real_data = wine_dataset['data']
    real_targets = wine_dataset['target']

    fake_features = []
    fake_targets = []

    for _ in range(n_rows):
        row_number = np.random.randint(0, len(real_data) - 1)
        fake_features.append(real_data[row_number])
        fake_targets.append(real_targets[row_number])

    features = pd.DataFrame(fake_features)
    targets = pd.DataFrame(fake_targets)
    return features, targets


@click.command("generate")
@click.option("--out_path", default="../data/raw")
def fake_generator(out_path: str) -> None:
    os.makedirs(out_path, exist_ok=True)
    features, targets = gen_fake_dataset(SIZE_DATASET)
    features.to_csv(os.path.join(out_path, NAME_FEATURES), index=False)
    targets.to_csv(os.path.join(out_path, NAME_TARGETS), index=False)


if __name__ == "__main__":
    fake_generator()
