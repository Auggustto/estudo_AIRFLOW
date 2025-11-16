## O que é Apache Airflow?

Apache Airflow é uma plataforma open-source para orquestração de workflows, permitindo criar, agendar e monitorar pipelines de dados de forma programática usando Python.

**Principais características:**

- Workflows definidos como código (Python)
- Interface web para monitoramento
- Escalável e extensível
- Suporte a execução paralela
- Sistema de retry e alertas

---

## Conceitos Fundamentais

### DAG (Directed Acyclic Graph)

Grafo acíclico direcionado que representa o workflow. Cada nó é uma tarefa e as arestas definem dependências.

### Task

Unidade básica de trabalho no Airflow. Pode ser:

- **Operators**: PythonOperator, BashOperator, etc.
- **Sensors**: Aguardam condições específicas
- **TaskFlow API**: Decoradores Python (@task)

### Scheduler

Componente que agenda e dispara as execuções das DAGs.

### Executor

Define como as tarefas são executadas (LocalExecutor, CeleryExecutor, KubernetesExecutor).

### Webserver

Interface web para monitoramento e gerenciamento.