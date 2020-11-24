# country-code-demo
## Command line
Usage: `python ./country_code.py --help` 

## Kubernetes
Pod and services files are in `/k8s/`
```
kubectl apply -f k8s/pods.yaml
kubectl apply -f k8s/services.yaml
```


## Monitoring via Grafana and Prometheus
Launched using helm: 
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add stable https://charts.helm.sh/stable
helm repo update
helm install prom prometheus-community/kube-prometheus-stack --namespace monitoring
```

Access by setting up port forwarding:
`kubectl port-forward $(kubectl get pods -l app.kubernetes.io/name=grafana -n monitoring -o name) --namespace monitoring 3000`

Grafana is running at http://localhost:3000
user: admin 
pass: prom-operator