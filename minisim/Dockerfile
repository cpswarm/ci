FROM maven:3-jdk-8-slim

RUN addgroup --gid 1000 minisim && \
    adduser --uid 1000 --ingroup minisim --system minisim

USER minisim

WORKDIR /home/minisim
VOLUME /home/minisim

ENTRYPOINT ["mvn", "test"]

## Running locally:
## SimulationWrapper
# git clone https://git.repository-pert.ismb.it/CPSwarm/SimulationWrapper.git
# docker build -t simulation-wrapper .
# docker run -v $(pwd)/SimulationWrapper:/home/minisim simulation-wrapper -Dtest_broker=tcp://test.mosquitto.org:1883
## WrappedMinisim
# git clone https://git.repository-pert.ismb.it/CPSwarm/WrappedMinisim.git
# docker build -t wrapped-minisim .
# docker run -v $(pwd)/WrappedMinisim:/home/minisim wrapped-minisim -Dtest_broker=tcp://test.mosquitto.org:1883