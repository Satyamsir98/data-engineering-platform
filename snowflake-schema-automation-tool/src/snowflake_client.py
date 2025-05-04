# import snowflake.connector


# def get_connection(schema):
#     return snowflake.connector.connect(
#         user="YOUR_USER",
#         password="YOUR_PASSWORD",
#         account="YOUR_ACCOUNT",
#         warehouse="YOUR_WAREHOUSE",
#         database="TEST_DB",
#         schema=schema
#     )


# def fetch_ddl(table_name):
#     conn = get_connection("PUBLIC")
#     cursor = conn.cursor()

#     try:
#         query = f"SELECT GET_DDL('TABLE', '{table_name}')"
#         cursor.execute(query)
#         return cursor.fetchone()[0]
#     finally:
#         cursor.close()
#         conn.close()


# def execute_ddl(ddl, schema):
#     conn = get_connection(schema)
#     cursor = conn.cursor()

#     try:
#         cursor.execute(ddl)
#     finally:
#         cursor.close()
#         conn.close()

from src.utils import log


def get_connection(schema):
    # Mock connection
    log(f"[MOCK] Connecting to Snowflake schema: {schema}")
    return None


def fetch_ddl(table_name):
    log(f"[MOCK] Fetching DDL for {table_name}")

    return f"""
    CREATE TABLE {table_name} (
        ID INT,
        NAME STRING
    );
    """


def execute_ddl(ddl, schema):
    log(f"[MOCK EXECUTE] Deploying to {schema}")
    print(ddl)