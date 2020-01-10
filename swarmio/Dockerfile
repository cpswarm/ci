FROM ubuntu:xenial

RUN apt update && apt -yq install gnupg2 
RUN add-apt-repository universe && add-apt-repository multiverse && apt update
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu xenial main" > /etc/apt/sources.list.d/ros-latest.list'
RUN apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
RUN apt update && DEBIAN_FRONTEND=noninteractive apt -yq install clang cmake git rsync fakeroot g++-aarch64-linux-gnu multistrap g++-arm-linux-gnueabihf ros-kinetic-ros-base
RUN rosdep init && rosdep update && source /opt/ros/kinetic/setup.bash
RUN apt -yq install python-rosinstall python-rosinstall-generator python-wstool build-essential 

COPY . /home
WORKDIR /home/build

RUN cmake .. -DSWARMIO_BUILD_MODE=PACKAGE
RUN cmake --build .
RUN cmake .. -DSWARMIO_TARGET_ARCHITECTURE=amd64 -DSWARMIO_BUILD_MODE=PACKAGE -DSWARMIO_MULTISTRAP_CONFIGURATION=xenial-ros -DSWARMIO_BUILD_ROS_NODE=ON
RUN cmake --build .
RUN cmake .. -DSWARMIO_TARGET_ARCHITECTURE=arm64 -DSWARMIO_BUILD_MODE=PACKAGE -DSWARMIO_MULTISTRAP_CONFIGURATION=xenial-ros -DSWARMIO_BUILD_ROS_NODE=ON
ENV CC aarch64-linux-gnu-g++
RUN cmake --build .
RUN cmake .. -DSWARMIO_TARGET_ARCHITECTURE=armhf -DSWARMIO_BUILD_MODE=PACKAGE -DSWARMIO_MULTISTRAP_CONFIGURATION=xenial-ros -DSWARMIO_BUILD_ROS_NODE=ON
ENV CC arm-linux-gnueabihf-g++
RUN cmake --build .

# Run test script
RUN ./libswarmio-amd64/src/libswarmio-build/logparser.py
