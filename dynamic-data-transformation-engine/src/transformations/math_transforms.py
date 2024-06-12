from src.transformations.base import TransformationBase

class RoundTransformation(TransformationBase):
    def apply(self, df, config):
        decimals = int(config.get("params", 0))
        for col in config["columns"]:
            out = config.get("output_column", f"{col}_round")
            df[out] = df[col].astype(float).round(decimals)
        return df


class AbsTransformation(TransformationBase):
    def apply(self, df, config):
        for col in config["columns"]:
            out = config.get("output_column", f"{col}_abs")
            df[out] = df[col].astype(float).abs()
        return df