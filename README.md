## This app used for checking Prometheus metrics on python docker for EKS ##

- git clone https://github.com/chapaya/mypromflask.git
- docker build -t chapaya/python-prometheus-app .
- docker login
- docker push chapaya/python-prometheus-app
- docker run -p 8000:8000 -p 5000:5000 chapaya/python-prometheus-app

Open:
- http://localhost:5000/
- http://localhost:8000/

## Deploy on k8s ##

- kubectl apply -f deployment.yaml
- kubectl get pod

## Configure Prometheus to scarp ##


# By Eran G #

	#!/bin/sh
	#deploy helm values in rancher
	echo "Show contexts ..."
	kubectl config get-contexts
	echo
	kubectl get po
	echo
	echo "Deploy helm ..."
	helm upgrade my-prom-stack kube-prometheus-stack -f kube-prometheus-stack/values.yaml --reset-values
	echo
	kubectl get po
	echo
	echo "Delete the pods.."
	kubectl delete po prometheus-my-prom-stack-kube-prometh-prometheus-0
	kubectl delete po alertmanager-my-prom-stack-kube-prometh-alertmanager-0
	echo
	echo "Show the pods..."
	sleep 5
	kubectl get po

# Create helm chart
- helm create python-prometheus-app-by-helm
- Create templates/deployment.yaml, templates/serivce.yaml,values.yaml
- helm install python-prometheus-app-by-helm ./python-prometheus-app
- or with custom-values.yaml : helm install python-prometheus-app-by-helm ./python-prometheus-app -f custom-values.yaml
- helm ls
- update in needed : helm upgarde python-prometheus-app-by-helm ./python-prometheus-app
- uninstall : helm uninstall python-prometheus-app-by-helm
