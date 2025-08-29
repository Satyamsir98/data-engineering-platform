from src.workflow_engine import run_workflow_sequence
from src.utils import log


def orchestrate():
    workflow_sequence = "wf1,wf2,wf3"

    log("AI Workflow Orchestration is starting")

    run_workflow_sequence(workflow_sequence)

    log("All workflows completed successfully")