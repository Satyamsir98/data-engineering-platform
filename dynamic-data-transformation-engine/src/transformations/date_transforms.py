from src.transformations.base import TransformationBase
import pandas as pd

class ToDateTransformation(TransformationBase):
    def apply(self, df, config):
        for col in config["columns"]:
            out = config.get("output_column", f"{col}_date")
            df[out] = pd.to_datetime(df[col])
        return df