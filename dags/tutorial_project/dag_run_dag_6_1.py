from airflow.sdk import dag, task
import pendulum
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.operators.bash import BashOperator

@dag(
    dag_id="trigger_dagrun2",
    description="usando o operator que inicia outra dag",
    schedule="15 18 * * *",
    start_date=pendulum.datetime(2026,4,2, tz="America/Sao_Paulo"),
    catchup=False,
    tags=["trigger_dagrun", "6_1"]
)
def my_dag():
    
    @task.bash
    def task_bash(command:str=None):
        return command
   
    task_bash("echo 'trigger dag run' && sleep 10") >> task_bash("echo '{{dag_run.conf['chave']}}' && sleep 50")
    
    
dag = my_dag()