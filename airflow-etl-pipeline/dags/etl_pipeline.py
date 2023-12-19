from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from src.extract import extract
from src.transform import transform
from src.load import load


def etl():
    df = extract()
    df = transform(df)
    load(df)


default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 1, 1),
}


with DAG(
    dag_id="cloud_agnostic_etl",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    run_etl = PythonOperator(
        task_id="run_etl",
        python_callable=etl,
    )