from airflow.sdk import task
from airflow.utils.trigger_rule import TriggerRule

class BashOperatorFactory():
    
    def __init__(self,task_id:str="id task;", command:str="echo 'insira um comando bash'", trigger_rule:TriggerRule=TriggerRule.ALL_DONE):
        self.task_id = task_id
        self.command = command
        self.trigger_rule = trigger_rule
        
    def build(self):

        @task.bash(task_id=self.task_id, trigger_rule=self.trigger_rule)
        def _task():
            return self.command

        return _task()