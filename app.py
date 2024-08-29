from flask import Flask
from prometheus_client import start_http_server, Counter, Summary

app = Flask(__name__)

# Prometheus metrics to track
REQUEST_COUNT = Counter('request_count', 'Total number of requests')
REQUEST_LATENCY = Summary('request_latency_seconds', 'Request latency')

@app.route('/')
def hello_world():
    REQUEST_COUNT.inc()  # Increment the request count
    with REQUEST_LATENCY.time():
        return "Hi from my python-Prometheus container"

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    # Start Flask application on port 5000
    app.run(host='0.0.0.0', port=5000)
