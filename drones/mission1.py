#Name: Tasha Margie Musau
#Date: 11/03/2026

#Program demonstrates mission one of a drone

from pysimverse import Drone
import time


drone = Drone(speed = 1000)
drone.connect()

drone.take_off(100)

drone.move_forward(250)
drone.move_right(250)

drone.land()

