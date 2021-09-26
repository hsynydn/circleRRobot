from math import cos
from math import sin
from math import radians
from math import degrees

from numpy import array
from threading import Thread
from time import sleep


class Controller(Thread):

    def __init__(self, robot):

        Thread.__init__(self)

        self.robot = robot

        self.inverse_jacobian = array([[0.0, 0.0], [0.0, 0.0]])

        # velocity - px/second
        self.x_dot = 0.0
        self.y_dot = 20.0

        #
        self.velocity_timer = 0

        self.theta1 = self.robot.theta1
        self.theta2 = self.robot.theta2

    def calculate_jacobian(self, theta1, theta2):

        # convert angles in degrees into angles in radians
        r_theta1 = radians(theta1)
        r_theta2 = radians(theta2)

        j11 = -self.robot.a4 * sin(r_theta1) * cos(r_theta2) - self.robot.a4 * cos(r_theta1) * sin(r_theta2) - self.robot.a2 * sin(r_theta1)
        j12 = -self.robot.a4 * sin(r_theta1) * cos(r_theta2) - self.robot.a4 * cos(r_theta1) * sin(r_theta2)
        j21 = self.robot.a4 * cos(r_theta1) * cos(r_theta2) - self.robot.a4 * sin(r_theta1) * sin(r_theta2) + self.robot.a2 * cos(r_theta1)
        j22 = self.robot.a4 * cos(r_theta1) * cos(r_theta2) - self.robot.a4 * sin(r_theta1) * sin(r_theta2)

        multiplier = 1.0/(j11 * j22 - j12 * j21)

        j11_inverse = multiplier * j22
        j12_inverse = multiplier * -j12
        j21_inverse = multiplier * -j21
        j22_inverse = multiplier * j11

        self.inverse_jacobian[0][0] = j11_inverse
        self.inverse_jacobian[0][1] = j12_inverse
        self.inverse_jacobian[1][0] = j21_inverse
        self.inverse_jacobian[1][1] = j22_inverse

    def set_velocity(self):

        self.x_dot = 200.0 * sin(radians(self.velocity_timer))
        self.y_dot = 200.0 * cos(radians(self.velocity_timer))

        self.velocity_timer += 1

    def run(self):

        sleep(2)

        counter = 0

        while True:

            counter += 1
            if counter == 360:
                print("self.robot.resetToInitialPosition()")
                self.theta1 = self.robot.resetΘ1
                self.theta2 = self.robot.resetΘ2
                counter = 0

            self.set_velocity()

            self.robot.command(self.theta1, self.theta2)

            self.calculate_jacobian(self.theta1, self.theta2)

            theta1_dot = degrees(self.inverse_jacobian[0][0] * self.x_dot + self.inverse_jacobian[0][1] * self.y_dot)
            theta2_dot = degrees(self.inverse_jacobian[1][0] * self.x_dot + self.inverse_jacobian[1][1] * self.y_dot)

            inc_theta1 = theta1_dot/100
            inc_theta2 = theta2_dot/100

            self.theta1 += inc_theta1
            self.theta2 += inc_theta2

            sleep(0.01) # 10ms
