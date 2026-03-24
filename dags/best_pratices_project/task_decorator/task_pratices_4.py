from airflow.sdk import task

@task.bash
def task_factory(task_id:str='id_task', command:str='echo "faça o input de um comando bash"'):
    return command