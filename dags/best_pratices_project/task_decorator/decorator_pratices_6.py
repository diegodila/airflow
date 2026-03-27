from airflow.sdk import dag, task_group
from airflow.utils.trigger_rule import TriggerRule
import pendulum
from airflow.providers.standard.operators.empty import EmptyOperator
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
    
    @task_group(group_id='load_database')
    def tg1():
        t3 = EmptyOperator(task_id='task_group3')
        t4 = EmptyOperator(task_id='task_group4')
        t5 = OperatorsFactory("meu_id_5", "echo 'task group aqui'", TriggerRule.ALL_DONE).build("bash")
        t6 = OperatorsFactory("meu_id_6", "hello taskgroup", TriggerRule.ALL_DONE).build("python")
        [t3 >> t4 >> t5] >> t6
    
    
    t1 >> tg1() >> t2
dag = my_dag()
    