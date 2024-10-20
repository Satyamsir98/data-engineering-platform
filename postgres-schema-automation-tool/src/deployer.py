from src.db_client import execute_ddl
from src.ddl_processor import qualify_schema
from src.utils import log

def deploy_schema(ddl_data, schema):
    for item in ddl_data:
        ddl = qualify_schema(item["ddl"], schema)

        log(f"Deploying {item['table']}")
        execute_ddl(ddl)