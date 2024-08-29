## This app used for checking Prometheus metrics on python docker for EKS ##

- git clone https://github.com/chapaya/mypromflask.git
- docker build -t chapaya/python-prometheus-app .
- docker login
- docker push chapaya/python-prometheus-app
- docker run -p 8000:8000 -p 5000:5000 chapaya/python-prometheus-app

Open:
http://localhost:5000/
http://localhost:8000/
