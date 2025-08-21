# Simple Python Load Balancer

A lightweight reverse proxy load balancer built with Python sockets to showcase
basic networking concepts for internship/demo purposes.

---

## Features
- Distributes requests across multiple backend servers using **Round-Robin** scheduling.
- Handles multiple clients concurrently using **threads**.
- Includes a **health checker** to skip unhealthy backends automatically.
- Tracks **request metrics** for each backend.
- Easy to run locally – no external infrastructure required.

## Installation
```bash
git clone <your-repo-url>
cd load-balancer
cd clients && pip install -r requirements.txt 


---

Usage

1. Start Backend Servers
Run each in separate terminals:
python3 backend_servers/server1.py
python3 backend_servers/server2.py
python3 backend_servers/server3.py

2. Start Load Balancer
python3 load_balancer/balancer.py

3. Send Requests
Using curl:  curl http://127.0.0.1:4000
Or run the test client:  python3 clients/client.py


Demo

Requests will be distributed across Server1, Server2, and Server3.

If a server is stopped, the health checker automatically removes it from rotation
