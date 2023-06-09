#!/usr/bin/env python3
from control_msgs.msg import JointControllerState
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64
import rospy
import control
import math
import numpy as np

mass_cart = 20.0
mass_pole = 2.0
length_pole = 0.5
g = 9.81

A = np.matrix([[0,1,0,0],
               [0, 0, -mass_pole*g/mass_cart, 0],
               [0, 0, 0, 1],
               [0, 0, (1 + mass_pole/mass_cart)*g/length_pole, 0]
               ])
B = np.matrix([ [0],
                [1/mass_cart],
                [0],
                [-1/mass_cart/length_pole]
                ])

# Tuning

# Q = np.diag( [1000.,0.,1000.,0.] )
# R = 20.0

#Q = np.diag( [1000.,0.,10000.,0.] )
#R = 10.0

# Final values of Q & R
Q = np.diag( [100.,0.,10000.,0.] )
R = 2.5

# Control law
K, S, E = control.lqr( A, B, Q, R )

# LQR Control of cart pole ROS node
class Cartpolesystem:
    def __init__(self):
        rospy.init_node('lqrcontrol')
        self.command_pub = rospy.Publisher("/invpend/joint1_velocity_controller/command",
                                            Float64, queue_size=10)
        self.theta_sub = rospy.Subscriber("/invpend/joint2_position_controller/state",
                                          JointControllerState, self.angles)
        self.pos_sub = rospy.Subscriber("/invpend/joint_states",
                                        JointState, self.pos_callback)
        self.current_state = np.array([0., 0., 0., 0.])
        self.desired_state = np.array([0., 0., 0., 0.])
        self.command_msg = Float64()
    
    def angles(self, angle_value):
        self.current_state[2] = angle_value.process_value
        self.current_state[3] = angle_value.process_value_dot
        
    def pos_callback(self, pase_value):
        self.current_state[0] = pase_value.position[1]
        self.current_state[1] = pase_value.velocity[1]
        
    def lqrcontrol(self):
        print("Pole in control with LQR")
        print("Steadt state error: {}".format(self.desired_state[2] - self.current_state[2]))
        self.command_msg.data = np.matmul(K, (self.desired_state - self.current_state))
        self.command_pub.publish(self.command_msg)
       

if __name__ == '__main__':
    lqr = Cartpolesystem()
    while not rospy.is_shutdown():
        lqr.lqrcontrol()  