## This could be the base image to run tests related to Modelio
FROM ubuntu:16.04

MAINTAINER Junhong LIANG <junhong.liang@fit.fraunhofer.de>

ENV MODELIO_PKG_NAME=modelio

## Install Modelio as Debian package
## Beside, xvfb is installed to create a virtual display for Modelio 

RUN apt-get update && \
    apt-get install -y wget && \
    mkdir /modelio && \
    wget -O /modelio/${MODELIO_PKG_NAME}.deb https://www.modelio.org/download/send/24-modelio-361/91-modelio-361-debian-ubuntu-64-bit.html  && \
    apt install -y /modelio/${MODELIO_PKG_NAME}.deb && \
    apt-get install -y xvfb
    
## The following command would create a virtual display with Xvfb and then generate files according to the project setting
CMD Xvfb :1 -screen 0 1024x768x16 & DISPLAY=:1.0 modelio-open-source3.6 -consoleLog -workspace /modelio -project  EmergencyExitRos -batch /modelio/launchGeneration.py

