from src.utils import log
from src.parser import parse_text_to_table

def process(file_path):
    log("Processing using Azure Form Recognizer flow")

    with open(file_path) as f:
        lines = f.readlines()

    df = parse_text_to_table(lines)

    log("Layout + OCR processing completed")
    return df