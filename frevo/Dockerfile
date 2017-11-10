FROM openjdk:8-jre-slim

RUN apt update && apt install -y git

ARG GIT_USER
ARG GIT_PASS

COPY testsuite /home/testsuite

WORKDIR /home
RUN git clone https://${GIT_USER}:${GIT_PASS}@git.repository-pert.ismb.it/mrappaport/cpswarm.git
RUN mv testsuite cpswarm/frevo

WORKDIR cpswarm/frevo
RUN java -jar createscripts.jar

CMD bash