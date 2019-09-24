# Code Generator CI

## Test
```bash
git clone https://github.com/cpswarm/ci.git
cd ci/cg
git clone https://github.com/cpswarm/code-generator.git repo
docker build -f Dockerfile-test .
```

## Build
```bash
git clone https://github.com/cpswarm/ci.git
cd ci/cg
git clone https://github.com/cpswarm/code-generator.git repo
docker build -t cpswarm/cg-builder -f Dockerfile-build .
```

#### Extract built artifacts
Create a container with the built image and from there, copy the artifacts
```bash
docker create --name cg-builder cpswarm/cg-builder
docker cp cg-builder:/home/target target
```
