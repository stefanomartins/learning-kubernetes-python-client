from kubernetes import client, config
import json

""" 
In case of SSL/TLS problems connecting to the Kubernetes cluster, uncomment the lines below and add `.clusters[].cluster.insecure-skip-tls-verify: true` in your kubeconfig file. Be advised that this is not recommended for production environments.
"""
import urllib3

urllib3.disable_warnings()

context = "my-context"
namespace = "my-namespace"

try:
    config.load_kube_config(context=context)
except:
    print("kubeconfig not available.")

v1 = client.NetworkingV1Api()

ingresses = v1.list_namespaced_ingress(namespace=namespace)
ingresses = [
    {"namespace": i.metadata.namespace, "name": i.metadata.name, "host": j.host}
    for i in ingresses.items
    for j in i.spec.rules
]
print(json.dumps(ingresses, indent=4))
