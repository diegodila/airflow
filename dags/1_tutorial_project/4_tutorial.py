import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(dag_id='Dag_4', 
         schedule=None, 
         start_date=pendulum.datetime(2026,3,13, tz='America/Sao_Paulo'),
         catchup=False,
        tags=['3 tag', '4 tag']
    ) as dag:
    task1 = BashOperator(task_id='task_A', bash_command="echo 'Diego'; echo 'Jose'; sleep 15")
    task2 = BashOperator(task_id='task_B', bash_command="echo 'Parei' && sleep 10")
    
    task1 >> task2