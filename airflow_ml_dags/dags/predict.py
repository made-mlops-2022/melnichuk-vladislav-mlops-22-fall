from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
# from airflow.sensors.python import PythonSensor


from utilities import (
        MOUNT_OBJECT, DIR_TRANSFORMER, DIR_MODEL,
        DIR_GENERATE, DIR_PREDICTIONS,
        DEFAULT_ARGS_USER, file_exists
)


with DAG(
        "predict",
        default_args=DEFAULT_ARGS_USER,
        schedule_interval="@weekly",
        start_date=days_ago(0),
) as dag:

    predict = DockerOperator(
        image="airflow-predict",
        command=f"--source_path {DIR_GENERATE} --out_path {DIR_PREDICTIONS} "
                f"--transformer_path {DIR_TRANSFORMER} --model_path {DIR_MODEL}",
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        network_mode="bridge",
        mounts=MOUNT_OBJECT
    )

    predict
