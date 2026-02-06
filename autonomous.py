#This is the Autonomous Code
#Import CoDrone EDU Libraries
from codrone_edu.drone import *

#Connect to drone and takeoff to ~36in
drone = Drone()
drone.pair()

drone.takeoff()

#Begin by taking off, turning off LED, ascending, and going through first key-hole
drone.set_drone_LED(0,0,0,100)
drone.send_absolute_position(0, 0, 1.5, 1.37, 0, 0)
#drone.hover(5)
drone.set_yaw(0)
drone.move_forward(distance=1.85, units="m", speed=1)
drone.set_yaw(0)

#Go Down, make sure we are aligned with top panel hole
drone.send_absolute_position(1.85, 0, 0.6, 0.5, 0, 0)
drone.set_yaw(0)
drone.send_absolute_position(1.85, 0, 0.6, 0.5, 0, 0)

#Get First Mat Color, and show by changing both drone and controller colors.
color_data = drone.get_back_color("rgb")
print(color_data)
drone.set_drone_LED(*color_data, brightness = 255)
drone.set_controller_LED(*color_data, brightness = 255)

#Ensure alignment, and Go Through Smaller Top Hole in Panel
drone.send_absolute_position(1.85, 0, 0.6, 0.5, 0, 0)
drone.send_absolute_position(3.7, 0, 0.6, 0.5, 0, 0)

#Get Second Mat Color, and show by changing both drone and controller colors.
color_data = drone.get_back_color("rgb")
print(color_data)
drone.set_drone_LED(*color_data, brightness = 255)
drone.set_controller_LED(*color_data, brightness = 255)

#End code with a land and close
drone.land()

drone.close()