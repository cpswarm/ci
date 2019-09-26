FROM ubuntu:bionic

RUN apt update && apt -y install clang cmake git rsync fakeroot

COPY . /home

WORKDIR /home/build

RUN cmake .. -DSWARMIO_BUILD_MODE=PACKAGE
RUN cmake --build .


