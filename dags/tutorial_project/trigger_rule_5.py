from airflow.sdk import dag, task
import pendulum
from airflow.utils.trigger_rule import TriggerRule

@dag(
    dag_id="dag_trigger_rule_5",
    description="usando o parametro de trigger rule",
    schedule="00 22 * * *",
    start_date=pendulum.datetime(2026,3,23, tz="America/Sao_Paulo"),
    catchup=False,
    tags=["trigger", "5"]
)
def my_dag():
    
    @task.bash
    def task_bash(task_id="task1", command:str=None, trigger_rule=None):
        return command
    
    task_bash("task1", "echo 'trigger5'",trigger_rule=TriggerRule.ONE_FAILED) >> task_bash("task2", "echo 'trigger10'")
    
    
dag = my_dag()