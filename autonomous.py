#This is the Autonomous Code
from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()

#Phase 1
drone.set_drone_LED(0,0,255,100)
drone.move_distance(0, 0, 0.9,1)
drone.hover(5)
drone.set_yaw(0)
drone.move_forward(distance=1.7, units="m", speed=1)
drone.set_yaw(0)

#Reading Color Mat to end Phase 1
color_data = drone.get_back_color("rgb")
print(color_data)
drone.set_drone_LED(*color_data)
#note, after research putting * "unpacks it"
#so then it won't dump it in like ((r, g, b)) but instead like (r,g,b)
#must be tested
drone.hover(5)

#Phase 2
drone.move_forward(distance=?, units="m", speed=1)
drone.move_distance(0, ?, 0,1)
drone.move_forward(distance=?, units="m", speed=1)
drone.move_distance(0, ?, 0,1)
drone.move_forward(distance=?, units="m", speed=1)

#Reading Color Mat to end Phase 2
color_data = drone.get_back_color("rgb")
print(color_data)
drone.set_drone_LED(*color_data)

#Phase 3
drone.move_distance(0, 0, ?,1)
drone.move_forward(distance=?, units="m", speed=1)
#code to align to not bump into yellow keyhole
drone.move_distance(0, 0, ?,1)
drone.move_distance(0, ?, 0,1)
drone.move_forward(distance=?, units="m", speed=1)
#code to align with bullseye for more points

drone.land()

drone.close()