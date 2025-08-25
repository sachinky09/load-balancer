import socket
import time

HOST = '127.0.0.1'
PORT = 5003 

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Server3 running on {HOST}:{PORT}\n")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if not data:
                    continue
                time.sleep(2)  
                response = b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello from Server3\n"
                conn.sendall(response)

if __name__ == "__main__":
    start_server()
