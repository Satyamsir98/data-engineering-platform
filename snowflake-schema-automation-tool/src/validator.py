from src.snowflake_client import get_connection
from src.utils import log


# def check_table_exists(conn, table):
#     cursor = conn.cursor()
#     query = f"""
#         SELECT 1 FROM INFORMATION_SCHEMA.TABLES
#         WHERE UPPER(TABLE_NAME) = UPPER('{table}')
#     """
#     cursor.execute(query)
#     result = cursor.fetchone()
#     cursor.close()
#     return bool(result)


# def fetch_columns(conn, table):
#     cursor = conn.cursor()
#     query = f"""
#         SELECT COLUMN_NAME, DATA_TYPE
#         FROM INFORMATION_SCHEMA.COLUMNS
#         WHERE TABLE_NAME = '{table}'
#     """
#     cursor.execute(query)
#     data = {row[0]: row[1] for row in cursor.fetchall()}
#     cursor.close()
#     return data


# def get_primary_keys(conn, table):
#     cursor = conn.cursor()
#     cursor.execute(f"SHOW PRIMARY KEYS IN TABLE {table}")
#     result = {row[3] for row in cursor.fetchall()}
#     cursor.close()
#     return result


# def get_foreign_keys(conn, table):
#     cursor = conn.cursor()
#     cursor.execute(f"SHOW IMPORTED KEYS IN TABLE {table}")
#     result = {(row[3], row[6], row[7]) for row in cursor.fetchall()}
#     cursor.close()
#     return result


# def validate_schema(tables, source_schema, target_schema):
#     source_conn = get_connection(source_schema)
#     target_conn = get_connection(target_schema)

#     report = []

#     for table in tables:
#         log(f"Validating {table}")

#         if not check_table_exists(source_conn, table):
#             report.append((table, "Table Exists", "Missing in Source"))
#             continue

#         if not check_table_exists(target_conn, table):
#             report.append((table, "Table Exists", "Missing in Target"))
#             continue

#         report.append((table, "Table Exists", "Success"))

#         # Column check
#         source_cols = fetch_columns(source_conn, table)
#         target_cols = fetch_columns(target_conn, table)

#         if source_cols == target_cols:
#             report.append((table, "Column Compare", "Success"))
#         else:
#             report.append((table, "Column Compare", "Mismatch"))

#         # Primary key
#         if get_primary_keys(source_conn, table) == get_primary_keys(target_conn, table):
#             report.append((table, "Primary Key", "Success"))
#         else:
#             report.append((table, "Primary Key", "Mismatch"))

#         # Foreign key
#         if get_foreign_keys(source_conn, table) == get_foreign_keys(target_conn, table):
#             report.append((table, "Foreign Key", "Success"))
#         else:
#             report.append((table, "Foreign Key", "Mismatch"))

#     source_conn.close()
#     target_conn.close()

#     return report



from src.utils import log


def validate_schema(tables, source_schema, target_schema):
    """
    Mock validation (no Snowflake required)
    """
    report = []

    for table in tables:
        log(f"[MOCK] Validating {table}")

        # Simulate validations
        report.append((table, "Table Exists", "Success"))
        report.append((table, "Column Compare", "Success"))
        report.append((table, "Primary Key", "Success"))
        report.append((table, "Foreign Key", "Success"))

    return report