from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.helpers import chain, cross_downstream
from datetime import datetime

with DAG("example_chain", start_date=datetime(2024, 1, 1), schedule=None):

    op1 = EmptyOperator(task_id="op1")
    op2 = EmptyOperator(task_id="op2")
    op3 = EmptyOperator(task_id="op3")
    op4 = EmptyOperator(task_id="op4")

    # op1 → op2 → op3 → op4
    chain(op1, op2, op3, op4)
