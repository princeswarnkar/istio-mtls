# Istio-mTLS 
2 Deployments with mTLS and monitoring feature.

We shall require a running kubernetes cluster ( Here we are using minikube cluster)

## Installing Minikube in local system >>

Please follow link: https://minikube.sigs.k8s.io/docs/start/ to install minikube binaries in your local.

Once you install minikube binary, please run below command to install minikube with required resources:

minikube start --cpus=4 --memory=8g --kubernetes-version=1.20.0 --driver=docker

*Istio recommend to have 8g of memory in cluster*

