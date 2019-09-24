# Simulation & Optimization Orchestrator CI

## Test
First, add the private key to communicate with the test server and the Kubernetes cluster configuration file.

Then: 
```bash
git clone https://github.com/cpswarm/ci.git cpswarm_ci
git clone https://github.com/cpswarm/SimulationOrchestrator.git soo
cp cpswarm_ci/soo/Dockerfile-test soo/Dockerfile-test
cd soo
docker build -f Dockerfile-test .
```

## Build
```bash
git clone https://github.com/cpswarm/ci.git cpswarm_ci
git clone https://github.com/cpswarm/SimulationOrchestrator.git soo
cp cpswarm_ci/soo/Dockerfile-install soo/Dockerfile-install
cd soo
docker build -t cpswarm/soo-builder -f Dockerfile-install .
```

#### Extract built artifacts
Create a container with the built image and from there, copy the artifacts
```bash
docker create --name soo-builder cpswarm/soo-builder
docker cp soo-builder:/home/target target
```
