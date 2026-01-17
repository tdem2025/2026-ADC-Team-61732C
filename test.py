#Python Test Code To Learn The Basics Of Coding CoDrone EDU
#This just has the drone do basic movements (takeoff, turn left and right,go up and down, and forward and back, and land).
#Just make any lines you want to disable a comment
#imports codrone edu libraries
from codrone_edu.drone import *

drone = Drone()
drone.pair() # pair automatically, may not always work
# if drone.pair doesn't work then try drone.pair(port_name = 'COM3')    # pair with a specific port (Must be set??)

drone.takeoff()

drone.hover(5)
#rotate to the left 90 degrees
drone.turn_left(90)
drone.hover(5)
#rotate to the right 90 degrees
drone.turn_right(90)
drone.hover(5)
#ascend 0.25 meters
drone.move_distance(0, 0, 0.3, 1)
drone.hover(5)
#descend 0.25 meters
drone.move_distance(0, 0, -0.3, 1)
drone.hover(5)
#fly forward 1 foot
drone.move_forward(distance=0.3, units="m", speed=1)
drone.hover(5)
#fly backward 1 foot
drone.move_backward(distance=0.3, units="m", speed=1)
drone.hover(5)
#fly left 1 foot
drone.move_left(distance=0.3, units="m", speed=1)
drone.hover(5)
#fly right 1 foot
drone.move_right(distance=0.3, units="m", speed=1)
drone.hover(5)

drone.land()
#closes connection between controller and program
drone.close()