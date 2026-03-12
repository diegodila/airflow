from datetime import datetime
import pendulum

from airflow.sdk import DAG, task
from airflow.providers.standard.operators.bash import BashOperator

local_tz = pendulum.timezone("America/Sao_Paulo")

# A Dag represents a workflow, a collection of tasks
with DAG(dag_id="amarilis", start_date=datetime(2026, 3, 11, tzinfo=local_tz), schedule="55 21 * * *", catchup=False) as dag:
    # Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task()
    def airflow():
        print("airflow")
        print(datetime.now())

    # Set dependencies between tasks
    hello >> airflow()