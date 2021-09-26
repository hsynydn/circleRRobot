from robot.gui import *
from robot.robot import *
from control.controller import *

# make configurations of robot
# arg1 - arm length 1
# arg2 - arm length 2
# arg3 - x placement of robot in coordinate system
# arg4 - y placement of robot in coordinate system
# arg5 - init theta1
# arg6 - init theta2
myRobot = Robot(200, 200, 400, 400, 100, 100)

# controller gives commands to follow specified path
# controller runs on another thread
controller = Controller(myRobot)
controller.start()

# gui run on main thread
gui = GUI(myRobot)
gui.start()


