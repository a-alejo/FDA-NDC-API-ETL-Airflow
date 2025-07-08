import sys

sys.path.insert(0, "/opt/airflow")
sys.path.insert(0, "/opt/airflow/src")

from extract import extract_data
from load import load_data
from transform import transform_data

from config import api_key
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

dag = DAG(
    dag_id="etl_pipeline",
    description="ETL pipeline that extracts FDA NDC data and loads to Postgres DB",
    start_date=datetime(2025, 2, 15),
    schedule="@daily",
    default_args={
        "owner": "airflow",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    catchup=False,
    tags=["ETL", "FDA", "Postgres"],
)

# Task 1: Extract data
extract_task = PythonOperator(
    task_id="extract_data", python_callable=extract_data, dag=dag
)

# Task 2: Transform data
transform_task = PythonOperator(
    task_id="transform_data", python_callable=transform_data, dag=dag
)

# Task 3: Load data
load_task = PythonOperator(task_id="load_data", python_callable=load_data, dag=dag)

# Set task dependencies
extract_task >> transform_task >> load_task
