import pandas as pd
from utils.helpers import load_config
from utils.logger import log


def run_silver():
    config = load_config()

    bronze_path = config["paths"]["bronze"]
    silver_path = config["paths"]["silver"]

    df = pd.read_csv(bronze_path)

    log("Transforming data for Silver layer")

    # Cleaning
    df = df.dropna()
    df["amount"] = df["amount"].astype(float)

    df.to_csv(silver_path, index=False)

    log(f"Silver data written to {silver_path}")