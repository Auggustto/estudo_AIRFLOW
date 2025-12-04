import datetime
from airflow.sdk import DAG, dag
from airflow.providers.standard.operators.empty import EmptyOperator

"""
1° Há três maneiras de declarar um Dag: você pode usar withuma instrução (gerenciador de contexto), q
ue adicionará qualquer coisa dentro dele ao Dag implicitamente:
"""

with DAG(
    dag_id="my_dag_name",
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
):
    EmptyOperator(task_id="task")
    
"""
2° pode usar um construtor padrão, passando o Dag para qualquer operador que você usar:
"""
my_dag = DAG(
    dag_id="my_dag_name",
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
)
EmptyOperator(task_id="task", dag=my_dag)


"""
3° você pode usar o @dagdecorador para transformar uma função em um gerador de Dag :
"""
@dag(start_date=datetime.datetime(2021, 1, 1), schedule="@daily")
def generate_dag():
    EmptyOperator(task_id="task")


generate_dag()