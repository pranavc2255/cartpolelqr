# cartpolelqr
Created LQR control ROS python script based on following cart-pole github: https://github.com/linZHank/invpend_experiment

## Setup
> My configuration was Ubuntu 20.04LTS, ROS-Noetic and Gazebo\-11.0. Other combinations of Linux, ROS and Gazebo may work, but not guaranteed.
1. cd to the `/catkin_ws` directory in ROS workspace (e.g. `cd ~/catkin_ws/`)
2. `git clone https://github.com/pranavc2255/cartpolelqr'
3. `catkin build` if you were using [Catkin Command Line Tools](https://catkin-tools.readthedocs.io/en/latest/)
4. `source ~/catkin_ws/devel/setup.bash`
5. run `roslaunch invpend_control load_invpend.launch` to spawn the model in gazebo and initiate ros_control

## Tuning the PID pole position (angle) controller, and regulate the pole angle at horizontal position.
1. To launch rqt for PID control run and tune PID in the GUI by running: `rosrun rqt_reconfigure rqt_reconfigure`
2. Run this to publish pole angle: `rostopic pub -r5 /invpend/joint2_position_controller/command std_msgs/Float64 "data: 1.57"`

[![IMAGE ALT TEXT HERE](https://i9.ytimg.com/vi_webp/Pix90YIE1u0/mq1.webp?sqp=CNyr6qAG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLC8pEdVtUgs1-j-qJEZ_9fkifHL0Q)](https://youtu.be/Pix90YIE1u0)

## Running LQR control
1. To run lqr control go to `cd ~/catkin_ws/src/invpend_experiment/invpend_control/scripts` and run: `python3 lqr_cartpole.py`
2. You can tune Q & R matrices according to your environment for better control performance.
