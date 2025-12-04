from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG("example_set_downstream", start_date=datetime(2024, 1, 1), schedule=None):

    first = EmptyOperator(task_id="first")
    second = EmptyOperator(task_id="second")
    third = EmptyOperator(task_id="third")
    fourth = EmptyOperator(task_id="fourth")

    first.set_downstream([second, third])
    third.set_upstream(fourth)
