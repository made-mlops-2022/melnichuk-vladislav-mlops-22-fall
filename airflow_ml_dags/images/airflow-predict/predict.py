import os
import pandas as pd
import pickle
import click

NAME_DATA = "features.csv"
NAME_PREDICT = "predict.csv"
NAME_TRANSFORMER = "transform.pkl"
NAME_MODEL = "model.pkl"


@click.command("predict")
@click.option("--source_path", default="../data/raw")
@click.option("--out_path", default="../data/predictions")
@click.option("--transformer_path", default="../data/transformer_model/transform.pkl")
@click.option("--model_path", default="../data/models/model.pkl")
def predict(source_path: str, out_path: str, transformer_path: str, model_path: str) -> None:
    os.makedirs(source_path, exist_ok=True)
    os.makedirs(out_path, exist_ok=True)

    data = pd.read_csv(os.path.join(source_path, NAME_DATA))

    with open(os.path.join(transformer_path, NAME_TRANSFORMER), 'rb') as file_obj:
        transformer = pickle.load(file_obj)
    with open(os.path.join(model_path, NAME_MODEL), 'rb') as file_obj:
        model = pickle.load(file_obj)

    transform_data = pd.DataFrame(transformer.fit_transform(data))
    predictions = pd.DataFrame(model.predict(transform_data))
    predictions.to_csv(os.path.join(out_path, NAME_PREDICT), index=False)


if __name__ == '__main__':
    predict()
