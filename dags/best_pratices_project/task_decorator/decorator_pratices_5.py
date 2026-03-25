from airflow.sdk import dag
import pendulum
from best_pratices_project.task_decorator.task_pratices_5 import BashOperatorFactory
from airflow.utils.trigger_rule import TriggerRule


@dag(
    dag_id='dag_task_factory_class_5',
    description='criando uma dag com decorator e task factory com class',
    schedule="10 22 * * *",
    start_date=pendulum.datetime(2026,3,1, tz="America/Sao_Paulo"),
    catchup=False,
    tags=['class', 'dag5']
)
def my_dag():
    
    t1 = BashOperatorFactory('id_01', 'echo "class dag 5"').build()
    t2 = BashOperatorFactory('id_02', 'echo "task 2 executada"', TriggerRule.ALL_FAILED).build()
    
    t1 >> t2
dag = my_dag()