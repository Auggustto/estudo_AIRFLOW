from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.helpers import chain
from datetime import datetime

with DAG("example_chain_dynamic", start_date=datetime(2024, 1, 1), schedule=None):

    tasks = [EmptyOperator(task_id=f"op{i}") for i in range(1, 6)]

    chain(*tasks)
