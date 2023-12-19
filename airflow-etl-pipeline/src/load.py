import json
from src.cloud_io import write_data


def load(df):
    with open("config/config.json") as f:
        config = json.load(f)

    write_data(df, config["output_path"], config["cloud"])