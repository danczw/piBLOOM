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

    # delete resources
    sudo microk8s.kubectl delete all --all -n {namespace}

    # create piBLOOM kubernetes deployment resources
    sudo microk8s.kubectl create -f pibloom-api-deployment.yaml,pibloom-proxy-deployment.yaml,pibloom-web-deployment.yaml,pinet-networkpolicy.yaml,pibloom-api-service.yaml,pibloom-proxy-service.yaml,pibloom-web-service.yaml
    # shorter test
    sudo microk8s.kubectl create -f pibloom-web-deployment.yaml,pibloom-web-service.yaml,pibloom-ingress.yaml
    # delete piBLOOM kubernetes deployment resources
    sudo microk8s.kubectl delete -f pibloom-api-deployment.yaml,pibloom-proxy-deployment.yaml,pibloom-web-deployment.yaml,pinet-networkpolicy.yaml,pibloom-api-service.yaml,pibloom-proxy-service.yaml,pibloom-web-service.yaml

    # install ingress controller
    # sudo microk8s.kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.3.1/deploy/static/provider/cloud/deploy.yaml
    sudo microk8s enable ingress
    # enable load balancer
    sudo microk8s enable metallb:192.168.178.70-192.168.178.80

    # run noip
    sudo /usr/local/bin/noip2
    sudo systemctl start noip2.service
    # check noip
    sudo noip2 -S
```