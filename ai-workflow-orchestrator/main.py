from src.orchestrator import orchestrate
from src.function_registry import register_function
from src.mock_services import (
    list_workflows,
    execute_workflow,
    get_workflow_status,
)

# Registering functions  for simulating AI function-calling
register_function("list_workflows", list_workflows)
register_function("execute_workflow", execute_workflow)
register_function("get_workflow_status", get_workflow_status)


if __name__ == "__main__":
    orchestrate()