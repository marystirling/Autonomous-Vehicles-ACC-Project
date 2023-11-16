# Autonomous-Vehicles-ACC-Project

### TEST DRIVE:
When running, the purpose of our project is to see if it can change the set speed with geographic positional information. For testing purposes, instead of relying on GPS and hard-coding this, we want to manually just input a new set speed. The command to do this while running our ros controller is this (changing out 50 for desired set speed:
```shell
rostopic pub -r 10 /new_set_speed std_msgs/Int16 "data: 50"
```

### SIMULINK FILES

1. ol_simulation.slx -> open loop simulation

2. cl_simulation.slx -> closed loop simulation

3. ros_controller.slx -> ros topics code generator

### TO SET UP DOCKER
1. Go to the directory where you have the Dockerfile downloaded. Make sure to have the bag file in the same directory and launch files downloaded in same directory.

2. Build the Docker container:

    ```shell
    docker build -t test:latest .
    ```

3. Create a Docker volume named `catkin_ws` using the following command:

    ```shell
    docker volume create catkin_ws
    ```

4. Run the container with the volume mounted using this command:

    ```shell
    docker run --mount type=bind,source=.,target=/catkin_ws -it test:latest
    ```

5. Change the directory to `catkin_ws` within the container:

    ```shell
    cd /catkin_ws
    ```

6. Build your ROS workspace:

    ```shell
    catkin_make
    ```



