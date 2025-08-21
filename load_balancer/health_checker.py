import socket
import threading
import time

class HealthChecker(threading.Thread):
    def __init__(self, backends, interval=5):
        super().__init__(daemon=True)
        self.backends = backends
        self.interval = interval

    def run(self):
        while True:
            for backend in self.backends:
                backend["alive"] = self.check_backend(backend)
            time.sleep(self.interval)

    def check_backend(self, backend):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect((backend["host"], backend["port"]))
            return True
        except:
            return False
