from airflow.sdk import dag, task
import pendulum
from airflow.utils.trigger_rule import TriggerRule
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.bash import BashOperator

@dag(
    dag_id="trigger_dagrun",
    description="usando o operator que inicia outra dag",
    schedule="00 22 * * *",
    start_date=pendulum.datetime(2026,4,2, tz="America/Sao_Paulo"),
    catchup=False,
    tags=["trigger_dagrun", "6"]
)
def my_dag():
    
    @task.bash
    def task_bash(command:str=None):
        return command
    
    task3 = TriggerDagRunOperator(
        task_id = 'task3',
        trigger_dag_id="trigger_dagrun2",
        conf={"chave":"Aiflow in here!"},
        wait_for_completion=True,
        poke_interval=5,
    )
    
    task_bash("echo 'trigger dag run'") >> task_bash("echo 'trigger 6'") >> task3
    
    
dag = my_dag()