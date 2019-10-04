FROM cpswarm/stage-simulator:1.0.3

RUN echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc \
		  && /bin/bash -c "source ~/.bashrc"

ENV ROS_PACKAGE_PATH /opt/ros/kinetic/share

COPY . $HOME

WORKDIR $HOME

RUN apt-get install psmisc
