import re

def qualify_schema(ddl, schema):
    pattern = re.compile(r"(?i)^CREATE TABLE ([\"\w]+)")
    match = pattern.search(ddl)

    if match:
        table = match.group(1)
        if "." not in table:
            ddl = ddl.replace(
                f"CREATE TABLE {table}",
                f"CREATE TABLE {schema}.{table}",
                1
            )
    return ddl