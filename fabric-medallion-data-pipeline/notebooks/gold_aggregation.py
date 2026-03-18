import pandas as pd
from utils.helpers import load_config
from utils.logger import log


def run_gold():
    config = load_config()

    silver_path = config["paths"]["silver"]
    gold_path = config["paths"]["gold"]

    df = pd.read_csv(silver_path)

    log("Aggregating data for Gold layer")

    result = df.groupby("product")["amount"].sum().reset_index()

    result.rename(columns={"amount": "total_sales"}, inplace=True)

    result.to_csv(gold_path, index=False)

    log(f"Gold data written to {gold_path}")