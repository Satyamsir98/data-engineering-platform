from src.transformations.string_transforms import *
from src.transformations.math_transforms import *
from src.transformations.date_transforms import *

TRANSFORMATION_REGISTRY = {
    "upper": UpperTransformation(),
    "lower": LowerTransformation(),
    "trim": TrimTransformation(),
    "length": LengthTransformation(),
    "concat": ConcatTransformation(),

    "round": RoundTransformation(),
    "abs": AbsTransformation(),

    "to_date": ToDateTransformation()
}