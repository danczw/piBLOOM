**Kubernetes Raspberry Pi Cluster Cmd Cheat Sheet**

```bash
    # test docker images w/o kubernetes
    sudo docker run -itd -p 8080:8080 danczw/pibloom-web
    sudo docker run -itd -p 8080:8080 danczw/pibloom-proxy
    sudo docker run -itd -p 8080:8080 danczw/pibloom-api

    # get kubernetes resources
    sudo microk8s.kubectl get nodes 
    sudo microk8s.kubectl get pods
    sudo microk8s.kubectl get pods -o=custom-columns=NAME:.metadata.name,STATUS:.status.phase,NODE:.spec.nodeName --all-namespaces
    sudo microk8s.kubectl get svc
    sudo microk8s.kubectl get deployments
    sudo microk8s.kubectl get deployments --all-namespaces
    sudo microk8s.kubectl get ingress
    sudo microk8s.kubectl get all

    # describe resources
    sudo microk8s.kubectl describe ingress pibloom-ingress

    # create piBLOOM kubernetes deployment resources
    sudo microk8s.kubectl create -f pibloom-api-deployment.yaml,pibloom-proxy-deployment.yaml,pibloom-web-deployment.yaml,pinet-networkpolicy.yaml,pibloom-api-service.yaml,pibloom-proxy-service.yaml,pibloom-web-service.yaml
    # delete piBLOOM kubernetes deployment resources
    sudo microk8s.kubectl delete -f pibloom-api-deployment.yaml,pibloom-proxy-deployment.yaml,pibloom-web-deployment.yaml,pinet-networkpolicy.yaml,pibloom-api-service.yaml,pibloom-proxy-service.yaml,pibloom-web-service.yaml

    # install ingress controller
    sudo microk8s.kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.3.1/deploy/static/provider/cloud/deploy.yaml
```