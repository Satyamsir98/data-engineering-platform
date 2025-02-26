import json
from src.aws_processor import process as aws_process
from src.azure_processor import process as azure_process


def run():
    with open("config/config.json") as f:
        config = json.load(f)

    cloud = config["cloud"]
    file_path = config["input_file"]

    if cloud == "aws":
        return aws_process(file_path)
    elif cloud == "azure":
        return azure_process(file_path)
    else:
        raise ValueError("Unsupported cloud")