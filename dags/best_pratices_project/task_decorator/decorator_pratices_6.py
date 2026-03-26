from airflow.sdk import dag
from airflow.utils.trigger_rule import TriggerRule
import pendulum
from best_pratices_project.task_decorator.task_pratices_6 import OperatorsFactory

@dag(
    dag_id='dag_task_group_class',
    description='criando uma dag com task group com class',
    schedule='00 22 * * *',
    start_date=pendulum.datetime(2026,3,25,tz="America/Sao_Paulo"),
    catchup=False,
    tags=['class', 'taskgroup']
)
def my_dag():
    
    t1 = OperatorsFactory("meu_id_1", "sleep 10", TriggerRule.ALL_DONE).build("bash")
    t2 = OperatorsFactory("meu_id_2","Diego",TriggerRule.ALL_DONE).build("python")
    
    
dag = my_dag()
    