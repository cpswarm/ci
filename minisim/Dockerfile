## Running locally:
## SimulationWrapper
# git clone https://git.repository-pert.ismb.it/CPSwarm/SimulationWrapper.git
# docker build -t simulation-wrapper .
# docker run -v /path-to-SimulationWrapper:/home simulation-wrapper -Dtest_broker=tcp://example.com:1883
## WrappedMinisim
# git clone https://git.repository-pert.ismb.it/CPSwarm/WrappedMinisim.git
# docker build -t wrapped-minisim .
# docker run -v /path-to-WrappedMinisim:/home wrapped-minisim -Dtest_broker=tcp://example.com:1883

FROM maven:3-jdk-8-alpine

WORKDIR /home
VOLUME /home

ENTRYPOINT ["mvn", "test"]
