from datetime import timedelta
from docker.types import Mount
import os


def file_exists(file_name: str) -> bool:
    return os.path.exists(file_name)

DIR_METRICS = "/data/metrics/{{ ds }}"
DIR_GENERATE = "/data/raw/{{ ds }}"
DIR_PREPROCESSED = "/data/processed/{{ ds }}"
DIR_TRANSFORMER = "/data/transformer_model/{{ ds }}"
DIR_MODEL = "/data/models/{{ ds }}"
DIR_PREDICTIONS = "/data/predictions/{{ ds }}"

SIZE_VAL = 0.15

DEFAULT_ARGS_USER = {
    "owner": "Melnichuk Vladislav",
    "email": ["vs.melnichuk09@gmail.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

MOUNT_OBJECT = [Mount(
    source="E:/Code/hws_mlops/repo/melnichuk-vladislav-mlops-22-fall/airflow_ml_dags/data",
    target="/data",
    type='bind'
    )]
