import threading
import requests
import json
from src.utils.logger import write_logs


def trigger_api(payload, url, timeout=5):

    def send_request():
        try:
            headers = {"Content-Type": "application/json"}
            requests.post(url, data=json.dumps(payload), headers=headers, timeout=timeout)
            write_logs("INFO", f"API triggered successfully: {url}")
        except Exception as e:
            write_logs("ERROR", f"API trigger failed: {str(e)}")

    thread = threading.Thread(target=send_request)
    thread.daemon = True
    thread.start()