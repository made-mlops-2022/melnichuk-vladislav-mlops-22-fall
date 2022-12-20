from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.utils.dates import days_ago
from utilities import MOUNT_OBJECT, DEFAULT_ARGS_USER

DIR_OUTPUT = "data/raw/{{ ds }}"

with DAG(
        "generator",
        default_args=DEFAULT_ARGS_USER,
        schedule_interval="@daily",
        start_date=days_ago(0),
) as dag:

    generate = DockerOperator(
        image="airflow-generate-data",
        command=f"--out_path {DIR_OUTPUT}",
        task_id="docker-airflow-generate-data",
        do_xcom_push=False,
        network_mode="bridge",
        auto_remove=True,
        mounts=MOUNT_OBJECT
    )

    generate
