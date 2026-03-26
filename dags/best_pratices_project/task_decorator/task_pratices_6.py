from airflow.sdk import task
from airflow.utils.trigger_rule import TriggerRule

class OperatorsFactory():
    
    def __init__(self,task_id:str="id task;", command:str="echo 'insira um comando bash'", trigger_rule:TriggerRule=TriggerRule.ALL_DONE):
        self.task_id = task_id
        self.command = command
        self.trigger_rule = trigger_rule
        
    def build(self,operator:str="bash"):

        if operator == "bash":
            @task.bash(task_id=self.task_id, trigger_rule=self.trigger_rule)
            def _task_bash():
                return self.command

            return _task_bash()
        elif operator == "python":
            
            @task(task_id=self.task_id, trigger_rule=self.trigger_rule)
            def _task_python():
                print(self.command)
                return 100 + 19
            return _task_python()
        else:
            raise ValueError("Use 'python' ou 'bash'")
        