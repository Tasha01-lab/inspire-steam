from robodk.robolink import *

#Connect to RoboDK
RDK = Robolink()

#Get robot
robot = RDK.Item('', ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception()

