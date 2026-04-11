from airflow.sdk import dag, task
import pendulum
from airflow.providers.smtp.operators.smtp import EmailOperator
import time

@dag(
    dag_id="dag_email_smtp_gmail",
    description="send emails to smtp gmail",
    schedule="00 22 * * *",
    start_date=pendulum.datetime(2026,4,8, tz="America/Sao_Paulo"),
    catchup=False,
    tags=['email', 'smtp']
)
def my_dag():
    
    # Generate 5 sleeping tasks, sleeping from 0.0 to 0.4 seconds respectively
    @task
    def my_sleeping_function(random_base):
        """This is a function that will run within the DAG execution"""
        time.sleep(random_base)

    for i in range(5):
        sleeping_task = my_sleeping_function.override(task_id=f"sleep_for_{i}")(random_base=i / 10)

        
    send_email = EmailOperator(
    task_id="send_email_test",
    to="ferreira.dfg@gmail.com",
    subject="Teste Airflow 2",
    html_content="<h3>Funcionou!</h3>",
    )
    
    sleeping_task >> send_email
    
dag = my_dag()