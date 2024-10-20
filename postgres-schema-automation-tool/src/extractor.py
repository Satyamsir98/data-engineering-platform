from src.db_client import fetch_ddl
from src.utils import log

def extract_schema(tables):
    ddl_data = []

    for t in tables:
        log(f"Extracting {t}")
        ddl = fetch_ddl(t)

        ddl_data.append({
            "table": t,
            "ddl": ddl
        })

    return ddl_data