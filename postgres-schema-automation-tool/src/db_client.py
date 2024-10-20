from src.utils import log

def get_connection(schema):
    log(f"[MOCK] Connecting to PostgreSQL schema: {schema}")
    return None


def fetch_ddl(table):
    log(f"[MOCK] Extracting DDL for {table}")
    return f"CREATE TABLE {table} (id INT, name TEXT);"


def execute_ddl(ddl):
    log(f"[MOCK EXECUTE]")
    print(ddl)