from codrone_edu.drone import *

drone = Drone()
drone.pair()

drone.takeoff()

drone.move_distance(0, 0, 0.9,1)
#drone.hover(5)
#drone.set_yaw(0)
#drone.move_forward(distance=1.7, units="m", speed=1)
drone.flip("back")
drone.hover(2)
drone.flip("back")
drone.hover(2)
drone.flip("back")
drone.hover(2)
drone.flip("back")
drone.hover(2)
drone.flip("back")
drone.hover(2)



drone.land()

drone.close()