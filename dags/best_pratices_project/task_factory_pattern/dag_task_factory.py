from airflow import DAG
from best_pratices_project.task_factory_pattern.task_factory import create_bash_task
import pendulum

with DAG(dag_id='dag_task_factory', schedule="08 21 * * *", start_date=pendulum.datetime(2026,3,16,tz='America/Sao_Paulo'), catchup=False) as dag:
    task1 = create_bash_task('task_id_bash_1', 'echo "task factory best pratices in airflow && sleep 10"')
    
    task2 = create_bash_task('task_id_bash_2', 'echo "task factory best pratices in airflow 2 && sleep 15"')
    
    task1 >> task2