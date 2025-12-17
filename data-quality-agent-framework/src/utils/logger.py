import datetime

def write_logs(level, message, step_param=None):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    step_info = f"[Step: {getattr(step_param, 'step_name', 'N/A')}]" if step_param else ""
    print(f"{timestamp} [{level}] {step_info} {message}")