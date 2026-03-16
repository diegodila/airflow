def create_bash_task(task_id:str, command:str) -> BashOperator :
    from airflow.operators.bash import BashOperator
    return BashOperator(task_id=task_id, bash_command=command)
    