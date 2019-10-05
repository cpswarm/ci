FROM cpswarm/gazebo-simulator:latest

LABEL io.k8s.description="Gazebo Simulation Manager with Xfce desktop and VNC Environment" \
      io.k8s.display-name="cpswarm/gazebo-em-ex with Xfce desktop and VNC Environment"

RUN echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc \
		  && /bin/bash -c "source ~/.bashrc"

ENV ROS_PACKAGE_PATH /opt/ros/kinetic/share

COPY . $HOME

WORKDIR $HOME

