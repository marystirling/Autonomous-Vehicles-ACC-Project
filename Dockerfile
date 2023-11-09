# syntax=docker/dockerfile:1
FROM ros:noetic-robot
# change the default shell command
SHELL ["/bin/bash", "-c"]
# this gets run in this image
RUN source ros_entrypoint.sh
# now add this to all future calls
RUN echo "source /ros_entrypoint.sh" >> /etc/bash.bashrc
# create our catkin workspace
RUN mkdir -p catkin_ws/src
# get the
RUN source /etc/bash.bashrc
# change to our working directory
WORKDIR catkin_ws
RUN source /ros_entrypoint.sh && catkin_make
# clone the packages we need
# get the git package
RUN apt-get -y update
RUN apt-get -y install git
WORKDIR /catkin_ws/src
RUN git clone https://github.com/jmscslgroup/profproject.git
RUN git clone https://github.com/jmscslgroup/carsimplesimulink.git
RUN git clone https://github.com/jmscslgroup/subtractor.git
RUN git clone https://github.com/jmscslgroup/odometer.git
#RUN git clone https://github.com/marystirling/Autonomous-Vehicles-ACC-Project.git
# you only get one command
# CMD roscore
