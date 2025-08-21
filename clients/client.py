import requests
import threading

URL = "http://127.0.0.1:4000"

def send_request(i):
    try:
        r = requests.get(URL)
        print(f"Request {i}: {r.text.strip()}")
    except Exception as e:
        print(f"Request {i} failed: {e}")

def main():
    threads = []
    for i in range(10):  # Send 10 concurrent requests
        t = threading.Thread(target=send_request, args=(i,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
