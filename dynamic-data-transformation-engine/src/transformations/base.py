class TransformationBase:
    def apply(self, df, config):
        raise NotImplementedError("Must implement apply method")