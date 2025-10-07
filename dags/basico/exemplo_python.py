# Para rodar código Python diretamente

from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def saudacao():
    print("🔥 Executando tarefa Python no Airflow!")

with DAG(
    'exemplo_python',
    start_date=datetime(2025, 10, 1),
    schedule=None,  # execução manual
    catchup=False,
) as dag:
    tarefa = PythonOperator(
        task_id='tarefa_saudacao',
        python_callable=saudacao
    )
