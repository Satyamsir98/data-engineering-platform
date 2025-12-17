from src.dq_agent import DQ_AGENT
from src.utils.helpers import load_config

if __name__ == "__main__":
    # config = load_config()

    agent = DQ_AGENT()

    mock_step_param = {
        "definitions": [
            {"step_name": "DQ Check 1", "df": "orders", "cloud": "aws"},
            {"step_name": "DQ Check 2", "df": "customers", "cloud": "azure"}
        ]
    }

    agent.execute(
        step_param=mock_step_param,
        execution_id="exec_001",
        client_name="demo_client",
        batch_name="batch_01",
        job_name="dq_job"
    )