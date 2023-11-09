# Autonomous-Vehicles-ACC-Project

Go to directory where tou have Dockerfile downloaded. Make sure to have the bag file in the same directory. Build the docker container:

docker build -t test:latest .

Run this command

docker volume create catkin_ws



Now run this container with it mounted:

docker run --mount type=bind,source=.,target=/catkin_ws -it test:latest

Now cd into catkin_ws and run 

catkin_make
