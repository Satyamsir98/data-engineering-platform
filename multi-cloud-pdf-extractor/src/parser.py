import pandas as pd

def parse_text_to_table(lines):
    lines = [l.strip() for l in lines if l.strip()]

    headers = lines[0].split()
    rows = []

    for line in lines[1:]:
        parts = line.split()
        if len(parts) == len(headers):
            rows.append(parts)

    return pd.DataFrame(rows, columns=headers)