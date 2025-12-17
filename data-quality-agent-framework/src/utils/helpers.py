import datetime
import yaml

def update_status_table(definition, execution_id, client_name, batch_name, job_name, table, db):
    step_dict = {
        "execution_id": execution_id,
        "client_name": client_name,
        "batch_name": batch_name,
        "job_name": job_name,
        "step_name": definition.get("step_name"),
        "start_time": str(datetime.datetime.now()),
        "status": "STARTED"
    }
    db.upsert(table, step_dict)
    return step_dict


def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)