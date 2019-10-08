FROM maven:3.6.2-jdk-11-slim

COPY . /home

WORKDIR /home/frevo/optimization-messages
RUN mvn install

WORKDIR /home/frevo/frevo-next
RUN mvn install

WORKDIR /home/frevo/frevo-cpp-exporter
RUN mvn install

WORKDIR /home/frevo/frevo-xmpp
RUN mvn install

