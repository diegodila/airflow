import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG (
    dag_id='My_DAG_ID',
    description="Minha terceira description par DAG",
    schedule=None,
    start_date= pendulum.datetime(2026,3,13, tz="America/Sao_Paulo"),
    catchup=False,
    tags=['3 tag', '4 tag']
) as dag:
    task1 = BashOperator(task_id='task1', bash_command="echo '3 comando'")
    task2 = BashOperator(task_id='task2', bash_command="sleep 10")
    task3 = BashOperator(task_id='task3', bash_command="echo '5 comando'")
    
    task1 >> task2 >> task3