#Name: Tasha Margie Musau
#Date: 11/03/2026

#Program demonstrates using python to manually control a drone

from pysimverse import Drone
import time
import keyboard

drone = Drone()
drone.connect()
time.sleep(1)

drone.take_off(5)
rc_speed = 250

while True:
    key = keyboard.read_key(1) & 0xff

    #get all values to zero
    left_right = 0
    forward_backward = 0
    up_down = 0
    yaw = 0

    if key == "w":
        forward_backward = rc_speed
    elif key == "s":
        forward_backward = -rc_speed
    elif key == "a":
        left_right = -rc_speed
    elif key == "d":
        left_right = rc_speed
    elif key == "c":
        up_down = -rc_speed
    elif key == "q":
        yaw = -1
    elif key == "e":
        yaw = 1
    elif key == "1" or key == 27:
        drone.land()
        time.sleep(2)
        break
        
    drone.send_rc_control(
        left_right,
        forward_backward,
        up_down,
        yaw
    )
