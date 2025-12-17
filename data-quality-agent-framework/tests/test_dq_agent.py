import unittest
from src.dq_agent import DQ_AGENT


class TestDQAgent(unittest.TestCase):

    def setUp(self):
        self.agent = DQ_AGENT()
        self.mock_step_param = {
            "definitions": [
                {"step_name": "Test Step 1", "df": "orders", "cloud": "aws"},
                {"step_name": "Test Step 2", "df": "customers", "cloud": "azure"}
            ]
        }

    def test_execute_runs_without_error(self):
        try:
            self.agent.execute(
                step_param=self.mock_step_param,
                execution_id="test_exec",
                client_name="test_client",
                batch_name="test_batch",
                job_name="test_job"
            )
            success = True
        except Exception as e:
            print(e)
            success = False

        self.assertTrue(success)


if __name__ == "__main__":
    unittest.main()