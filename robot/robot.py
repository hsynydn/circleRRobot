from math import cos
from math import sin
from math import degrees
from math import radians


# scara type manipulator without prismatic joint
class Robot:

    def __init__(self, a2, a4, origin_x, origin_y, theta1, theta2):

        # arm lengths in px
        self.a2 = a2
        self.a4 = a4

        # positions of joints
        self.joint1 = [origin_x, origin_y]
        self.joint2 = [0.0, 0.0]
        self.end_effector = [0.0, 0.0]

        # initialize turn angles
        self.theta1 = theta1
        self.theta2 = theta2

        self.resetΘ1 = theta1
        self.resetΘ2 = theta2

        self.calculate_position(self.theta1, self.theta2)

    def calculate_position(self, theta1, theta2):

        self.joint2[0] = self.a2 * cos(radians(theta1)) + self.joint1[0]
        self.joint2[1] = self.a2 * sin(radians(theta1)) + self.joint1[1]

        self.end_effector[0] = self.a4 * cos(radians(theta1 + theta2)) + self.joint2[0]
        self.end_effector[1] = self.a4 * sin(radians(theta1 + theta2)) + self.joint2[1]

    # function to command to the robot
    def command(self, theta1, theta2):
        self.theta1 = theta1
        self.theta2 = theta2

        self.calculate_position(self.theta1, self.theta2)

    def resetToInitialPosition(self):
        self.joint2[0] = self.a2 * cos(radians(self.resetΘ1)) + self.joint1[0]
        self.joint2[1] = self.a2 * sin(radians(self.resetΘ2)) + self.joint1[1]

        self.end_effector[0] = self.a4 * cos(radians(self.resetΘ1 + self.resetΘ2)) + self.joint2[0]
        self.end_effector[1] = self.a4 * sin(radians(self.resetΘ1 + self.resetΘ2)) + self.joint2[1]