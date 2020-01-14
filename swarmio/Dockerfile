FROM ros:kinetic-ros-base-xenial

COPY . /home
WORKDIR /home/build

RUN apt update && DEBIAN_FRONTEND=noninteractive apt -yq install clang cmake git rsync fakeroot multistrap g++-5-arm-linux-gnueabihf g++-5-multilib

RUN cmake .. -DSWARMIO_BUILD_MODE=PACKAGE
RUN cmake --build .
RUN cmake .. -DSWARMIO_TARGET_ARCHITECTURE=amd64 -DSWARMIO_BUILD_MODE=PACKAGE -DSWARMIO_BUILD_ROS_NODE=ON
RUN cmake --build .
RUN cmake .. -DSWARMIO_TARGET_ARCHITECTURE=armhf -DSWARMIO_BUILD_MODE=PACKAGE -DSWARMIO_MULTISTRAP_CONFIGURATION=xenial-ros -DSWARMIO_BUILD_ROS_NODE=ON
ENV CC arm-linux-gnueabihf-g++-5
RUN cmake --build .

# Run test script
RUN ./libswarmio-amd64/src/libswarmio-build/logparser.py
