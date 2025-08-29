import time
from datetime import datetime


def log(message, level="INFO"):
    """
    Simple logger function with timestamp
    """
    print(f"[{datetime.now()}] [{level}] {message}")


def retry(func, retries=3, delay=2, *args, **kwargs):
    """
    Retry wrapper for function calls
    """
    for attempt in range(1, retries + 1):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            log(f"Attempt {attempt} failed: {str(e)}", "ERROR")
            time.sleep(delay)
    raise Exception(f"Function failed after {retries} retries")


def poll_status(check_fn, execution_id, interval=2):
    """
    Poll workflow status until completion
    """
    while True:
        result = check_fn(execution_id=execution_id)
        status = result.get("status")

        log(f"Execution {execution_id} status: {status}")

        if status in ["Completed", "Failed"]:
            return status

        time.sleep(interval)


def generate_execution_id(workflow_id):
    """
    Generate mock execution ID
    """
    timestamp = int(time.time())
    return f"{workflow_id}_{timestamp}"