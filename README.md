# Autonomous-Vehicles-ACC-Project

Go to directory where tou have Dockerfile downloaded. Make sure to have the bag file in the same directory.

Run this command

docker volume create catkin_ws


Now run this container with it mounted:

docker run --mount type=bind,source=.,target=/catkin_ws -it test:latest
