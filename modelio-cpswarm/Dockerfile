FROM ubuntu:18.04

LABEL description="Docker Image for testing the CPSWarm Module" maintainer="Kais CHAABOUNI <kais.chaabouni@softeam.fr>"

ENV MODELIO_PKG_NAME=modelio

## Install Modelio as Debian package
## Beside, xvfb is installed to create a virtual display for Modelio 

RUN apt update && \
    apt install -yq wget xvfb && \
    mkdir /cpswarm-test && \
    wget -O /cpswarm-test/${MODELIO_PKG_NAME}.deb https://www.modelio.org/download/send/31-modelio-3-8-1/147-modelio-3-8-1-debian-ubuntu-64-bit.html && \
    apt install -yq /cpswarm-test/${MODELIO_PKG_NAME}.deb \
                unzip
    
## The following command would create a virtual display with Xvfb and then generate files according to the project setting

#CMD Xvfb :1 -screen 0 1024x768x16 & DISPLAY=:1.0 modelio-open-source3.8 -consoleLog -workspace /cpswarm-test/workspace/ -project modelio_test_project -batch /cpswarm-test/deploy-module.py

CMD /cpswarm-test/launch-test-scripts.sh

