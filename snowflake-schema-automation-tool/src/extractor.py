from src.snowflake_client import fetch_ddl
from src.utils import log


def extract_schema(tables):
    ddl_list = []

    for table in tables:
        log(f"Extracting DDL for {table}")
        ddl = fetch_ddl(table)

        ddl_list.append({
            "table_name": table,
            "ddl": ddl
        })

    return ddl_list