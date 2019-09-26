# Swarmio CI

## Build
```bash
git clone https://github.com/cpswarm/ci.git
git clone https://github.com/cpswarm/swarmio.git 
mv ci/swarmio/Dockerfile swarmio/Dockerfile
cd swarmio
docker build -t cpswarm/swarmio-builder .
```

#### Extract built artifacts
Create a container with the built image and from there, copy the artifacts
```bash
docker create --name swarmio-builder cpswarm/swarmio-builder
docker cp swarmio-builder:/home/build/packages packages
```
