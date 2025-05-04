from src.snowflake_client import execute_ddl
from src.ddl_processor import clean_ddl
from src.utils import log


def deploy_schema(ddl_data, target_schema):
    log(f"Deploying schema to {target_schema}")

    for item in ddl_data:
        table = item["table_name"]
        ddl = item["ddl"]

        cleaned_ddl = clean_ddl(ddl)

        log(f"Executing DDL for {table}")
        execute_ddl(cleaned_ddl, target_schema)

    log("Deployment completed successfully")