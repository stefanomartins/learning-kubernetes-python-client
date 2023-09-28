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

apps_v1_api = client.AppsV1Api()
deployments = apps_v1_api.list_namespaced_deployment(namespace=namespace)

# Using list comprehensions, a more elegant way to filter data.
deployments = [
    {"namespace": i.metadata.namespace, "name": i.metadata.name}
    for i in deployments.items
]
print(json.dumps(deployments, indent=4))

# Using a for loop.
# deployment_list = []
# for i in deployments.items:
#     namespace = i.metadata.namespace
#     name = i.metadata.name
#     deployment_list.append({'namespace': namespace, 'name': name})

# print(json.dumps(deployment_list, indent=4))