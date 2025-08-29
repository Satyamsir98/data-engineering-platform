from src.function_registry import call_function
from src.utils import log
import time


def run_workflow_sequence(workflow_sequence):
    workflows = call_function("list_workflows", workflow_sequence=workflow_sequence)

    log(f"Workflow sequence: {workflows}")

    for wf in workflows:
        log(f"Starting workflow: {wf}")

        result = call_function("execute_workflow", workflow_id=wf)
        exec_id = result["execution_id"]

        while True:
            response = call_function("get_workflow_status", execution_id=exec_id)
            status = response.get("status")

            log(f"{wf} status: {status}")

            if status == "Completed":
                log(f"Workflow {wf} completed")
                break

            elif status == "Failed":
                log(f"Workflow {wf} failed. Stopping execution.", "ERROR")
                return

            time.sleep(2)