FUNCTION_MAP = {}

def register_function(name, func):
    FUNCTION_MAP[name] = func

def call_function(name, **kwargs):
    if name not in FUNCTION_MAP:
        raise Exception(f"{name} not found")
    return FUNCTION_MAP[name](**kwargs)