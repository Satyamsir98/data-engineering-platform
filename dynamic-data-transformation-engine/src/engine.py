import pandas as pd
import json
from src.registry import TRANSFORMATION_REGISTRY
from src.utils import log


def run_engine():
    log("Loading data...")
    df = pd.read_csv("data/sample.csv")

    with open("config/config.json") as f:
        transformations = json.load(f)

    for t in transformations:
        t_type = t["type"]

        log(f"Applying transformation: {t_type}")

        transformer = TRANSFORMATION_REGISTRY.get(t_type)

        if transformer:
            df = transformer.apply(df, t)
        else:
            log(f"Unknown transformation: {t_type}")

    return df