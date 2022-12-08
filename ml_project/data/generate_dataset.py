from boto3 import client
from typing import Tuple, NoReturn
import pandas as pd
from sklearn.model_selection import train_test_split
from entities import SplitParameters


def download_raw_data_from_s3(bucket: str, path: str, output: str) -> NoReturn:
    client_s3 = client("s3")
    client_s3.download_file(bucket, path, output)


def read_data_pd(initial_path: str) -> pd.DataFrame:
    data_pd = pd.read_csv(initial_path)
    return data_pd


def split_data_train_val(
    input_data: pd.DataFrame, params: SplitParameters
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    data_train, data_val = train_test_split(
        input_data, test_size=params.size_val, random_state=params.random_state
    )
    return data_train, data_val
