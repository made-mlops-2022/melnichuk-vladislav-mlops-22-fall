from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
# from airflow.sensors.python import PythonSensor

from utilities import (
    SIZE_VAL, DIR_METRICS, DIR_GENERATE,
    DIR_PREPROCESSED, DIR_TRANSFORMER,
    DIR_MODEL, MOUNT_OBJECT, DEFAULT_ARGS_USER, file_exists
)


with DAG(
        "train",
        default_args=DEFAULT_ARGS_USER,
        schedule_interval="@weekly",
        start_date=days_ago(0),
) as dag:

    data_preprocess = DockerOperator(
        image="airflow-preprocess",
        command=f"--source_path {DIR_GENERATE} --out_path "
                f"{DIR_PREPROCESSED} --transform_path {DIR_TRANSFORMER}",
        task_id="docker-airflow-preprocess",
        do_xcom_push=False,
        network_mode="bridge",
        mounts=MOUNT_OBJECT
    )

    data_split = DockerOperator(
        image="airflow-split",
        command=f"--source_path {DIR_PREPROCESSED} --val_size {SIZE_VAL}",
        task_id="docker-airflow-split",
        do_xcom_push=False,
        network_mode="bridge",
        mounts=MOUNT_OBJECT
    )

    model_train = DockerOperator(
        image="airflow-train",
        command=f"--source_path {DIR_PREPROCESSED} --out_path {DIR_MODEL}",
        task_id="docker-airflow-train",
        do_xcom_push=False,
        network_mode="bridge",
        mounts=MOUNT_OBJECT
    )

    model_val = DockerOperator(
        image="airflow-validation",
        command=f"--model_source_path {DIR_MODEL} --data_source_path "
                f"{DIR_PREPROCESSED} --metric_path {DIR_METRICS}",
        task_id="docker-airflow-val",
        do_xcom_push=False,
        network_mode="bridge",
        mounts=MOUNT_OBJECT
    )

    data_preprocess >> data_split >> model_train >> model_val
