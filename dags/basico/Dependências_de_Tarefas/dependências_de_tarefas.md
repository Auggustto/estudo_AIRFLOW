### Os DAGs não são nada sem tarefas para executar, e estas geralmente vêm na forma de Operadores , Sensores ou TaskFlow .

Uma Tarefa/Operador geralmente não vive sozinho; ele tem dependências de outras tarefas (aquelas a montante dele), 
e outras tarefas dependem dele (aquelas a jusante dele). Declarar essas dependências entre tarefas é o que compõe a estrutura Dag.

Existem duas maneiras principais de declarar dependências de tarefas individuais. A recomendada é usar os operadores `>> and <<` :

```
first_task >> [second_task, third_task]
third_task << fourth_task
```

Ou você também pode usar os métodos set_upstreamand mais explícitos ***set_downstream***:

```
first_task.set_downstream([second_task, third_task])
third_task.set_upstream(fourth_task)
```

Existem também atalhos para declarar dependências mais complexas. Se você quiser fazer com que uma lista de tarefas dependa de outra lista de tarefas, 
não poderá usar nenhuma das abordagens acima, então precisará usar ***cross_downstream***:
```
from airflow.sdk import cross_downstream

# Replaces
[op1, op2] >> op3
[op1, op2] >> op4

cross_downstream([op1, op2], [op3, op4])
```
E se você quiser encadear dependências, pode usar ***chain***:

```
from airflow.sdk import chain

# Replaces
op1 >> op2 >> op3 >> op4
chain(op1, op2, op3, op4)
```
Chain também pode criar dependências aos pares para listas do mesmo tamanho (isso é diferente das dependências cruzadas criadas por ***cross_downstream*** !):

```
# You can also do it dynamically
chain(*[EmptyOperator(task_id=f"op{i}") for i in range(1, 6)])
```

### Resumo Rápido das Dependências
| Padrão                           | Significado                                  | Tipo                          |
| -------------------------------- | -------------------------------------------- | ----------------------------- |
| `A >> B`                         | A executa antes de B                         | Dependência simples           |
| `A >> [B, C]`                    | A antes de B e C                             | Fan-out                       |
| `A << B`                         | B antes de A                                 | Dependência simples invertida |
| `A.set_downstream([B, C])`       | Igual ao `>>`                                | Programático                  |
| `A.set_upstream(B)`              | Igual ao `<<`                                | Programático                  |
| `cross_downstream(list1, list2)` | Cada task de list1 liga a cada task de list2 | Fan-out/fan-in múltiplo       |
| `chain(A, B, C, D)`              | A → B → C → D                                | Pipeline linear               |
