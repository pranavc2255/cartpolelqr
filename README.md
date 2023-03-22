# cartpolelqr
Created LQR control ROS python script based on following cart-pole github: https://github.com/linZHank/invpend_experiment

## Setup
> My configuration was Ubuntu 20.04LTS, ROS-Noetic and Gazebo\-11.0. Other combinations of Linux, ROS and Gazebo may work, but not guaranteed.
1. cd to the `/catkin_ws` directory in ROS workspace (e.g. `cd ~/catkin_ws/`)
2. `git clone https://github.com/pranavc2255/cartpolelqr'
3. `cartin build` if you were using [Catkin Command Line Tools](https://catkin-tools.readthedocs.io/en/latest/)
4. `source ~/catkin_ws/devel/setup.bash`
5. run `roslaunch invpend_control load_invpend.launch` to spawn the model in gazebo and initiate ros_control
6. To run lqr control go to (~/catkin_ws/src/invpend_experiment/invpend_control/scripts) and run: 'python3 lqr_carpole.py'
7. You can tune Q & R matrices according to your environment for better control performance.