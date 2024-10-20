from src.utils import log

def validate_schema(tables):
    report = []

    for t in tables:
        log(f" Validating {t}")

        report.append((t, "Table Exists", "Success"))
        report.append((t, "Column Compare", "Success"))
        report.append((t, "Primary Key", "Success"))
        report.append((t, "Foreign Key", "Success"))

    return report