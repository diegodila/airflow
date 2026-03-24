from airflow.sdk import dag
import pendulum
from best_pratices_project.task_decorator.task_pratices_4 import task_factory
from datetime import timedelta

default_args = {
    "depends_on_past" : False,
    "email": "ferreira.dfg@gmail.com",
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=120)
}

@dag(dag_id='minha_dag_4',
     schedule='45 21 * * *',
     start_date=pendulum.datetime(2026,3,23, tz="America/Sao_Paulo"),
     default_args=default_args,
     catchup=False)
def my_dag():
    
    t1 = task_factory("id_bash_1", "echo 'Diego Gonçalves'")
    t2 = task_factory("id_bash_2", "echo 'XXXX'")

    t1 >> t2
    
    
dag = my_dag()   