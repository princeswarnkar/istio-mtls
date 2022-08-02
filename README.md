# Istio-mTLS 
2 Deployments with mTLS and monitoring feature.

We shall require a running kubernetes cluster ( Here we are using minikube cluster)

## Installing Minikube in local system >>

Please follow link: https://minikube.sigs.k8s.io/docs/start/ to install minikube binaries in your local.

Once you install minikube binary, please run below command to install minikube with required resources:

minikube start --cpus=4 --memory=8g --kubernetes-version=1.20.0 --driver=docker

*Note: Istio recommend to have 8g of memory in cluster*

Once cluster is UP, we need to configure metalLB loadbalancer in minikube so istio-ingresssgateway can use it to deploy dedicated ingress loadbalancer to accept outside cluster's traffic.

### Installing metalLB in minikube

Use below commands to install and configure metalLB:

1. **minikube profile list** *>> To check profile details. Please check the IP range of your minikube cluster. Let assume we have minikube ip: 192.168.49.2*
2. **minikube addons enable metallb** *>> To enable metallb addon.*
3. **minikube addons configure metallb** *>> To configure metallb (it will ask you to configure metallb loadbalancer IP range. I have used 192.168.49.10 to 192.168.49.20 . IP range shoud be within minikube controlplane IP range/subnet)*


## Istio Installation on kubernetes cluster >>

We will use istioclt to install istio in kubernetes. Please follow below steps:

1. **export ISTIO_VERSION=1.14.0**
2. **wget -c -nv https://github.com/istio/istio/releases/download/${ISTIO_VERSION}/istio-${ISTIO_VERSION}-linux-amd64.tar.gz**
3. **tar -xzf istio-${ISTIO_VERSION}-linux-amd64.tar.gz; cd istio-${ISTIO_VERSION}**
4. **./bin/istioctl install --set profile=demo –y** >> *Installation istio with demo profile*

Once you done installation, please label the 'default' namespace with istio-injection=enabled

5. **kubectl label namespace default istio-injection=enabled**

## Deploy Store and Cart applications with istio componentes in k8s default namespace >>

Clone this repo and follow below steps:

### Deploy Store service >>

**kubectl apply -f ./store**

Wait for atleast 2-3 minutes and check if all pods are running fine. Once they run healthy, access the service in browser at:
http://store.192.168.49.10.nip.io

### Deploy Cart Service >> 


**kubectl apply -f ./cart**

Wait for atleast 2-3 minutes and check if all pods are running fine. Once they run healthy, access the service in browser at:
http://cart.192.168.49.10.nip.io

## Generating traffic >>

Run below commands to generate moc traffic for testing traffic flow:

**while true; do curl -s -o /dev/null http://cart.192.168.49.10.nip.io; done** >> *Cart Service*

**while true; do curl -s -o /dev/null http://store.192.168.49.10.nip.io; done** >> *Store Service*

## Enable mTLS in k8s >>

**kubectl apply -f ./mtls-security.yaml** *>> By default it is deployed as a STRICT mode. We have STRICT, PERMISSIVE and DISABLE mode available*


## Test the traffic routing and mTLS in graph >>

To visualise traffic routing and service graph and maps, you need to deploy addons. Please follow below command to deploy grafana, kiali, jaeger etc. 

**kubectl apply -f samples/addons/**

Once all services are deployed successfully (Keep checking all service's pod status in "istio-system" namespace), run below respective commands to access dashboards:

**./bin/istioctl dashboard kiali** >> *To check service traffic routing and k8s object mapping.*

**./bin/istioctl dashboard jaeger** >> *To check all the trasenctions from different services*

**./bin/istioctl dashboard grafana** >> *To get monitor dashboard*

