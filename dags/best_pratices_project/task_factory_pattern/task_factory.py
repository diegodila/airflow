from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from airflow.operators.bash import BashOperator
    
def create_bash_task(task_id:str, command:str) -> "BashOperator" :
    from airflow.operators.bash import BashOperator
    return BashOperator(task_id=task_id, bash_command=command)
    