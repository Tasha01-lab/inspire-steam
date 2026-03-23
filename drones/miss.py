#Name: Tasha Margie Musau
#Date: 11/03/2026

#Program demonstrates mission two of a drone

from pysimverse import Drone
import time

drone = Drone(speed = 1000)
drone.connect()

drone.take_off(200)

# distance is in cm
left_right = 6
forward_backward = 10
up_down = 0

#in degrees
yaw = 0.1

while True:
    drone.send_rc_control(
        left_right = left_right,
        forward_backward = forward_backward,
        up_down = up_down,
        yaw = yaw
    )
    