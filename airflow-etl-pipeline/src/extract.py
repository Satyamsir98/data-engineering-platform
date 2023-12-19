import json
from src.cloud_io import read_data


def extract():
    with open("config/config.json") as f:
        config = json.load(f)

    df = read_data(config["input_path"], config["cloud"])
    return df