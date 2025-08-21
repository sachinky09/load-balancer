import threading

# Dictionary to track request count per backend
request_count = {}
lock = threading.Lock()

def log_request(backend):
    """
    Increment request count for a backend.
    """
    key = f"{backend['host']}:{backend['port']}"
    with lock:
        request_count[key] = request_count.get(key, 0) + 1
    print(f"[METRICS] {key} has handled {request_count[key]} requests.")
