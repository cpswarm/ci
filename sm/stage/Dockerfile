FROM cpswarm/stage-simulator:latest

RUN echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc

ENV ROS_PACKAGE_PATH /opt/ros/kinetic/share

COPY . $HOME

WORKDIR $HOME

RUN apt-get install psmisc
