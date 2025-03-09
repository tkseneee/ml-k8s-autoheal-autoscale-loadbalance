import requests
import json
import concurrent.futures

# API URL (Updated)
URL = "http://localhost:80/predict"

# JSON Payload
payload = {"features": [5.1, 3.5, 1.4, 0.2]}
headers = {"Content-Type": "application/json"}

# Function to send a single request
def send_request():
    response = requests.post(URL, json=payload, headers=headers)
    return response.status_code

# Load Testing with Multiple Requests
NUM_REQUESTS = 5000  # Total number of requests
MAX_WORKERS = 20     # Simulating concurrency

with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    results = list(executor.map(lambda _: send_request(), range(NUM_REQUESTS)))

# Summary
print(f"Total Requests Sent: {len(results)}")
print(f"Successful Requests: {results.count(200)}")
print(f"Failed Requests: {results.count(500)}")
