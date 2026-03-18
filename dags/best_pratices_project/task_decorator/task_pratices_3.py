from airflow.sdk import task
    
@task.bash()
def create_task_bash(
    task_id:str=None,
    command:str="echo 'Insira um comando'"
):
    return command