
from airflow import DAG
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'spark_example',
    default_args=default_args,
    description='A simple Spark DAG',
    schedule_interval=timedelta(days=1),
)

