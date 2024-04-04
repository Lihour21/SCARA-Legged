from __future__ import print_function
import odrive
from odrive.enums import *
import time

# Initialize a list to store error data
error_data = []

print("Finding an odrive...")
dev = odrive.find_any()

# Set your PID gains and control mode as you did previous ly
dev.axis0.controller.config.pos_gain = 10  
dev.axis0.controller.config.vel_gain = 0.25
dev.axis0.controller.config.vel_integrator_gain = 0.333  

dev.axis1.controller.config.pos_gain = 10  
dev.axis1.controller.config.vel_gain = 0.25 
dev.axis1.controller.config.vel_integrator_gain = 0.333  

# Increase the velocity limits for both axes
dev.axis0.controller.config.vel_limit = 11

# Further decrease the current limits for both axes for significantly less force
dev.axis0.motor.config.current_lim = 5  # Reduced from 5

# Increase the velocity limits for the second axis
dev.axis1.controller.config.vel_limit = 11

# Further decrease the current limits for the second axis for significantly less force
dev.axis1.motor.config.current_lim = 5  # Reduced from 5

round = 360 
D1 = Degree1 = 45 # 54 Degree
D2 = Degree2 = 0  # 0 Degree
D3 = Degree3 = 65 # 61 Degree
D4 = Degree4 = 36 # 36 Degree
D5 = Degree5 = 20 # 18 Degree
D6 = Degree6 = -90 # -90 Degree

try:
    while True:
        # Set the initial positions for both axes (1)
        dev.axis1.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL
        dev.axis1.controller.input_pos = D1/round  # Change this to your desired initial position (Right motor)(x1)(negative value)
        dev.axis0.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL
        dev.axis0.controller.input_pos = D2/round # Change this to  your desired initial position (Left motor)(x0)(positive value) 
        # Wait for a short time (e.g., 0.5 seconds) to stay in the first position
        # Wait for a short time (e.g., 0.5 seconds) to stay in the first position
        time.sleep(0.17)

        # Set the initial positions for both axes (2)
        dev.axis1.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL
        dev.axis1.controller.input_pos = D3/round  # Change this to your desired initial position (Right motor)(x1)(negative value)
        dev.axis0.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL
        dev.axis0.controller.input_pos = D4/round  # Change this to your desired initial position (Left motor)(x0)(positive value)
          # Wait for a short time (e.g., 0.5 seconds) to stay in the second position////
        time.sleep(0.17)

  # Set the initial positions for both axes (3)
        dev.axis1.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL
        dev.axis1.controller.input_pos = D5/round  # Change this to your desired initial position (Right motor)(x1)(negative value)
        dev.axis0.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL
        dev.axis0.controller.input_pos = D2/round  # Change this to your desired initial position (Left motor)(x0)(positive value)
         # Wait for a short time (e.g., 0.5 seconds) to stay in the second position
        time.sleep(0.17)
        
          # Set the initial positions for both axes (4)
        dev.axis1.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL
        dev.axis1.controller.input_pos = D2/round  # Change this to your desired initial position (Right motor)(x1)(negative value)
        dev.axis0.controller.config.control_mode = CONTROL_MODE_POSITION_CONTROL
        dev.axis0.controller.input_pos = D6/round  # Change this to your desired initial position (Left motor)(x0)(positive value)
        # Wait for a short time (e.g., 0.5 seconds) to stay in the second position
        time.sleep(0.17)

except KeyboardInterrupt:
    print("User interrupted the program")
    
#