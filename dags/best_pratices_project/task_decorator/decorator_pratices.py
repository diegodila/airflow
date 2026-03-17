from airflow.decorators import dag, task
import pendulum

@dag(
    dag_id="dag_decorators",
    start_date=pendulum.datetime(2026,3,14),
    schedule=None,
    catchup=False
)
def example_dag():

    @task
    def task1():
        print("hello")

    @task
    def task2():
        print("world")

    task1() >> task2()
    
dag = example_dag()
