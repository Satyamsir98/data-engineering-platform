from src.transformations.base import TransformationBase

class UpperTransformation(TransformationBase):
    def apply(self, df, config):
        for col in config["columns"]:
            out = config.get("output_column", f"{col}_upper")
            df[out] = df[col].str.upper()
        return df


class LowerTransformation(TransformationBase):
    def apply(self, df, config):
        for col in config["columns"]:
            out = config.get("output_column", f"{col}_lower")
            df[out] = df[col].str.lower()
        return df


class TrimTransformation(TransformationBase):
    def apply(self, df, config):
        for col in config["columns"]:
            out = config.get("output_column", f"{col}_trim")
            df[out] = df[col].str.strip()
        return df


class LengthTransformation(TransformationBase):
    def apply(self, df, config):
        for col in config["columns"]:
            out = config.get("output_column", f"{col}_length")
            df[out] = df[col].astype(str).str.len()
        return df


class ConcatTransformation(TransformationBase):
    def apply(self, df, config):
        cols = config["columns"]
        out = config["output_column"]
        df[out] = df[cols].astype(str).agg(" ".join, axis=1)
        return df