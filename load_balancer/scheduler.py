import threading

class RoundRobinScheduler:
    def __init__(self, backends):
        self.backends = backends
        self.index = 0
        self.lock = threading.Lock()

    def get_next_backend(self):
        with self.lock:
            if not self.backends:
                return None

            for _ in range(len(self.backends)):
                backend = self.backends[self.index]
                self.index = (self.index + 1) % len(self.backends)

                # Skip unhealthy backends
                if backend.get("alive", True):
                    return backend
            return None
