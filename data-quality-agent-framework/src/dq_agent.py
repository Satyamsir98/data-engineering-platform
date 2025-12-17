from src.utils.logger import write_logs
from src.utils.db import db_connection
from src.utils.helpers import update_status_table, load_config
from src.connectors.aws_s3 import write_to_s3
from src.connectors.azure_adls import write_to_adls
from src.services.api_trigger import trigger_api
import datetime


class DQ_AGENT:

    def execute(self, step_param, execution_id, client_name, batch_name, job_name):
        return self.process_data(step_param, execution_id, client_name, batch_name, job_name)

    def process_data(self, step_param, execution_id, client_name, batch_name, job_name):
        try:
            write_logs("INFO", "Inside DQ AGENT")

            config = load_config()
            api_url = config["api"]["endpoint"]

            db = db_connection()
            job_step_status_table = "job_step_status"

            for definition in step_param["definitions"]:
                write_logs("INFO", f"Processing step: {definition.get('step_name', 'UNKNOWN')}")

                step_dict = update_status_table(
                    definition, execution_id, client_name, batch_name, job_name, job_step_status_table, db
                )

                df_name = definition["df"]
                print(f"[MOCK SPARK] Reading DataFrame: {df_name}")

                cloud_tag = definition.get("cloud", config["cloud"]["default"])

                if cloud_tag == "aws":
                    base_path = config["cloud"]["aws"]["base_path"]
                    write_path = f"{base_path}/{client_name}/{job_name}/{df_name}"
                    write_to_s3(df_name, write_path)
                else:
                    base_path = config["cloud"]["azure"]["base_path"]
                    write_path = f"{base_path}/{client_name}/{job_name}/{df_name}"
                    write_to_adls(df_name, write_path)

                payload = {
                    "write_path": write_path,
                    "cloud_tag": cloud_tag,
                    "status": "SUCCESS"
                }

                timeout = config["api"]["timeout"]
                trigger_api(payload, api_url, timeout)

                step_dict["end_time"] = str(datetime.datetime.now())
                step_dict["status"] = "COMPLETED"
                db.upsert(job_step_status_table, step_dict)

        except Exception as error:
            write_logs("ERROR", f"Error in DQ Agent: {str(error)}")
            raise error