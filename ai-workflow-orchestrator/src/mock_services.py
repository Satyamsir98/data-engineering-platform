import time
import random

def list_workflows(workflow_sequence):
    return workflow_sequence.split(",")

def execute_workflow(workflow_id):
    print(f"Executing workflow {workflow_id}")
    return {"execution_id": f"exec_{workflow_id}"}

def get_workflow_status(execution_id):
    time.sleep(1)
    status = random.choice(["Running", "Completed", "Failed"])
    return {"status": status}