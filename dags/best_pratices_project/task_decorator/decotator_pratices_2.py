from airflow.decorators import dag, task
import pendulum

@dag(dag_id='dag_decorator_2',
     schedule="40 21 * * *",
     start_date=pendulum.datetime(2026,3,17, tz="America/Sao_Paulo"),
     catchup=False
     )
def my_dag():
    
    @task.bash()
    def task_bash_d():
        return "echo 'Diego'"
    
    @task.bash(task_id="id_task_bash")
    def task_bash_d2():
        return "echo 'task 2'"
    
    task_bash_d2() >> task_bash_d()
    
dag = my_dag()