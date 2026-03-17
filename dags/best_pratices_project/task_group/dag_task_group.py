from airflow import DAG
from airflow.utils.task_group import TaskGroup
from airflow.operators.bash import BashOperator
import pendulum

with DAG(
    dag_id="dag_task_group",
    schedule="40 21 * * *",
    catchup=False,
    start_date=pendulum.datetime(2026,3,16, tz="America/Sao_Paulo")
) as dag:
    

    with TaskGroup("extract_group") as extract:

        extract_api = BashOperator(
            task_id="extract_api",
            bash_command="echo api"
        )

        extract_db = BashOperator(
            task_id="extract_db",
            bash_command="echo db"
        )
        
    with TaskGroup("transform_group") as transform:

        extract_api = BashOperator(
            task_id="transform_data",
            bash_command="echo 'tranform api'"
        )

        extract_db = BashOperator(
            task_id="transform_db",
            bash_command="echo 'transform db'"
        )    

extract  >> transform