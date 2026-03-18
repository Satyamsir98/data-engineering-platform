import pandas as pd
from utils.helpers import load_config
from utils.logger import log


def run_bronze():
    config = load_config()

    input_path = config["paths"]["input"]
    bronze_path = config["paths"]["bronze"]

    df = pd.read_csv(input_path)

    log("Ingesting raw data into Bronze layer")

    df.to_csv(bronze_path, index=False)

    log(f"Bronze data written to {bronze_path}")