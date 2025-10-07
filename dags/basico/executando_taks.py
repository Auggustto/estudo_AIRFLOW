"""
Os DAGs não são nada sem tarefas para executar, e estas geralmente vêm na forma de Operadores , Sensores ou TaskFlow .

Uma Tarefa/Operador geralmente não vive sozinho; ele tem dependências de outras tarefas (aquelas a montante dele), 
e outras tarefas dependem dele (aquelas a jusante dele). Declarar essas dependências entre tarefas é o que compõe a estrutura Dag.

Existem duas maneiras principais de declarar dependências de tarefas individuais. A recomendada é usar os operadores >>and <<:
------------------------------------------------------
first_task >> [second_task, third_task]
third_task << fourth_task
------------------------------------------------------

Ou você também pode usar os métodos set_upstreamand mais explícitos set_downstream:
------------------------------------------------------
first_task.set_downstream([second_task, third_task])
third_task.set_upstream(fourth_task)
------------------------------------------------------
"""

