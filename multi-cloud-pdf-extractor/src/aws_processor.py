from src.utils import log
from src.parser import parse_text_to_table

def process(file_path):
    log("Processing using AWS Textract flow")

    with open(file_path) as f:
        lines = f.readlines()

    df = parse_text_to_table(lines)

    log("Table extracted successfully")
    return df