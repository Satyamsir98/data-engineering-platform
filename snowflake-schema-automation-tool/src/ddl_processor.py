import re


def clean_ddl(ddl):
    return re.sub(r'(\w+)\.(\w+)\.', '', ddl, flags=re.IGNORECASE)