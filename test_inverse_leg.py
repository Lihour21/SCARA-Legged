from __future__ import print_function
import sys
import math
import matplotlib.pyplot as plt
import time
import odrive
from odrive.enums import *


my_drive = odrive.find_any()

# Get references to the motors
motor1 = my_drive.axis0
motor2 = my_drive.axis1

# Set your PID1 gains and control mode as you did previously
motor1.controller.config.pos_gain = 10  #degrees per PWM value
motor1.controller.config.vel_gain = 0.25 #degrees per second per PWM value
motor1.controller.config.vel_integrator_gain = 0.333 #degrees per second per PWM-second.


# Set your PID2 gains and control mode as you did previously
motor2.controller.config.pos_gain = 10  #degrees per PWM value
motor2.controller.config.vel_gain = 0.25 #degrees per second per PWM value
motor2.controller.config.vel_integrator_gain = 0.333 #degrees per second per PWM-second.

# Increase the velocity limits for both axes1
motor2.controller.config.vel_limit = 11
# Further decrease the current limits for both axes for significantly less force
motor2.motor.config.current_lim = 5  # Reduced from 5

# Increase the velocity limits for both axes2
motor1.controller.config.vel_limit = 11
# Further decrease the current limits for both axes for significantly less force
motor1.motor.config.current_lim = 5  # Reduced from 5


d = 100  # Length between origin and the two motors
l1 = 100.0  # Length from motor to passive joints
l2 = 100.0  # Length from passive joints to end effector
l3 = 150
l4 = 150
r = 360

def calc_angles(x, y):
    a1 = math.sqrt((x + d/2)**2 + y**2)
    a2 = math.sqrt((x - d/2)**2 + y**2)

    alpha1 = math.atan2(y, x + d/2)
    alpha2 = math.atan2(y, x - d/2)

    b1 = (l1**2 + a1**2 - l3**2) / (2 * l1 * a1)
    beta1 = math.acos(b1)

    b2 = (l2**2 + a2**2 - l4**2) / (2 * l2 * a2)
    beta2 = math.acos(b2)

    #theta1 = (alpha1 + beta1) *180/math.pi #mode ++
    #theta2 = (alpha2 + beta2) *180/math.pi #mode ++
    theta1 = (alpha1 + beta1) *180/math.pi #mode +-
    theta2 = (alpha2 - beta2) *180/math.pi #mode +-
    #theta1 = (alpha1 - beta1) *180/math.pi #mode --
    #theta2 = (alpha2 - beta2) *180/math.pi #mode --
    return (theta1, theta2)
t = 0.0
T = 0.5
f = 1/T
w = 2*math.pi*f
while True:
    x = 50*math.cos(w*t)
    y = 50*math.sin(w*t)+150
    shoulder = calc_angles(x, y)
    print(shoulder)
    # time.sleep(1)

    theta1 = shoulder[0]  # Extract the x-coordinate from the shoulder angles
    theta2 = shoulder[1]  # Extract the y-coordinate from the shoulder angles

    my_drive.axis1.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL
    my_drive.axis1.controller.input_pos = (theta2-12) / r  # Set the x-coordinate as the input_pos for the right motor (negative value)
    my_drive.axis0.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL
    my_drive.axis0.controller.input_pos = (theta1-158) / r  # Set the y-coordinate as the input_pos for the left motor (positive value)
    t = t+.01
    time.sleep(0.01)


