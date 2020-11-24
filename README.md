# Country Code Demo

## Command Line
### Prerequisites
* python 3.7 or newer
* installed pip dependencies: `pip install --no-cache-dir -r requirements.txt`
### Usage
`python ./country_code.py --help` 

## Docker and Kubernetes
### Docker image
Docker image is built locally and pushed here:
`https://hub.docker.com/r/samnfulton/country-code-demo`
### K8s Config Files
Pod and services files are in `/k8s/`
```
kubectl apply -f k8s/pods.yaml
kubectl apply -f k8s/services.yaml
```

## Monitoring with Grafana and Prometheus
Launched using the prometheus-community helm chart: 
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://charts.helm.sh/stable
helm repo update
helm install prom prometheus-community/kube-prometheus-stack --namespace monitoring
```

Access by setting up port forwarding:
```
kubectl port-forward $(kubectl get pods -l app.kubernetes.io/name=grafana -n monitoring -o name) --namespace monitoring 3000
```

Grafana is running at http://localhost:3000
user: admin 
pass: prom-operator

## Next Steps: 
* Automate docker build/push with Github Actions
* Create proper endpoint for Grafana for access outside the cluster