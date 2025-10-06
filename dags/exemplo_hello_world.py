from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Configurações básicas da DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='exemplo_hello_world',
    default_args=default_args,
    description='Minha primeira DAG no Airflow',
    schedule='@daily',  # executa 1x por dia
    start_date=datetime(2025, 10, 1),
    catchup=False,
    tags=['exemplo', 'iniciante'],
) as dag:

    tarefa_1 = BashOperator(
        task_id='print_hello',
        bash_command='echo "👋 Olá mundo, Airflow está funcionando!"'
    )

    tarefa_2 = BashOperator(
        task_id='print_date',
        bash_command='date'
    )

    tarefa_1 >> tarefa_2  # Define a ordem de execução
