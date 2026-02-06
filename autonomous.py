#This is the Autonomous Code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()

#Phase 1

drone.set_drone_LED(0,0,0,100)
drone.send_absolute_position(0, 0, 1.5, 1.37, 0, 0)
#drone.hover(5)
drone.set_yaw(0)
drone.move_forward(distance=1.85, units="m", speed=1)
drone.set_yaw(0)

#Reading Color Mat to end Phase 1
drone.send_absolute_position(1.85, 0, 0.6, 0.5, 0, 0)
drone.set_yaw(0)
drone.send_absolute_position(1.85, 0, 0.6, 0.5, 0, 0)

#Get Color Mat Color
color_data = drone.get_back_color("rgb")
print(color_data)
drone.set_drone_LED(*color_data, brightness = 255)

drone.send_absolute_position(1.85, 0, 0.6, 0.5, 0, 0)
drone.send_absolute_position(3.7, 0, 0.6, 0.5, 0, 0)

#Get Color Mat Color
color_data = drone.get_back_color("rgb")
print(color_data)
drone.set_drone_LED(*color_data, brightness = 255)

#note, after research putting * "unpacks it"
#so then it won't dump it in like ((r, g, b)) but instead like (r,g,b)
#must be tested

drone.land()

drone.close()