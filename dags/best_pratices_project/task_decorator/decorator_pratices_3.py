from airflow.sdk import dag
import pendulum
from best_pratices_project.task_decorator.task_pratices_3 import create_task_bash

@dag(dag_id="dag_decorator_task_factory",
     schedule="45 22 * * *",
     start_date=pendulum.datetime(2026,3,17, tz="America/Sao_Paulo"),
     catchup=False,
     )
def my_dag():
    
    t1 = create_task_bash(task_id="meu_id_1", command="echo 'meu d'")
    t2 = create_task_bash(task_id="meu_id_2", command="echo 'meu b'")
    
    t1 >> t2
    
dag = my_dag()