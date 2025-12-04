from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

"""
Equivalente a:

first_task → second_task

first_task → third_task

fourth_task → third_task
"""
with DAG("example_bitshift", start_date=datetime(2024, 1, 1), schedule=None):

    first_task = EmptyOperator(task_id="first")
    second_task = EmptyOperator(task_id="second")
    third_task = EmptyOperator(task_id="third")
    fourth_task = EmptyOperator(task_id="fourth")

    # first → second e third
    first_task >> [second_task, third_task]

    # fourth → third
    third_task << fourth_task
