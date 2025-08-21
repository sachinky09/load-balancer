import socket
import threading
import json
import os
from scheduler import RoundRobinScheduler
from utils import log_request
from health_checker import HealthChecker

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.json")

HOST = "127.0.0.1"
PORT = 4000 
def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def handle_client(client_socket, scheduler):
    backend = scheduler.get_next_backend()
    if not backend:
        client_socket.sendall(b"HTTP/1.1 503 Service Unavailable\r\n\r\nNo backend available")
        client_socket.close()
        return

    backend_host = backend["host"]
    backend_port = backend["port"]

    try:
        data = client_socket.recv(4096)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as backend_socket:
            backend_socket.connect((backend_host, backend_port))
            backend_socket.sendall(data)
            response = backend_socket.recv(4096)

        client_socket.sendall(response)
        log_request(backend)
    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        client_socket.close()

def start_balancer():
    config = load_config()
    scheduler = RoundRobinScheduler(config["backends"])

    # Start health checker thread
    checker = HealthChecker(config["backends"], config["health_check_interval"])
    checker.start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Load Balancer running on {HOST}:{PORT}")

        while True:
            client_socket, addr = s.accept()
            threading.Thread(target=handle_client, args=(client_socket, scheduler)).start()

if __name__ == "__main__":
    start_balancer()
