class RobotDrawer:

    def __init__(self, robot):

        self.robot = robot

        self.canvas = None

        self.paint_list = []

    def set_canvas(self, canvas):
        self.canvas = canvas

    def refresh(self):

        self.canvas.delete("all")

        self.draw_arm(self.normalize(self.robot.joint1), self.normalize(self.robot.joint2))
        self.draw_arm(self.normalize(self.robot.joint2), self.normalize(self.robot.end_effector))

        self.draw_motor(self.normalize(self.robot.joint1))
        self.draw_motor(self.normalize(self.robot.joint2))

        self.draw_paint(self.normalize(self.robot.end_effector))

        self.draw_end_effector(self.normalize(self.robot.end_effector))

    def draw_motor(self, position):
        self.canvas.create_oval(position[0] - 10, position[1] - 10, position[0] + 10, position[1] + 10, fill="red", outline="red")

    def draw_arm(self, position1, position2):
        self.canvas.create_line(position1[0], position1[1], position2[0], position2[1], width=2, fill="white")

    def draw_end_effector(self, position):
        self.canvas.create_oval(position[0] - 2, position[1] - 2, position[0] + 2, position[1] + 2, fill="red")

    def draw_paint(self, position):

        k = [0, 0]
        k[0] = position[0]
        k[1] = position[1]

        if k not in self.paint_list:
            self.paint_list.append(k)

           # print("robot - ", [self.robot.joint1, self.robot.joint2, self.robot.end_effector])
           # print(self.paint_list[0], [self.paint_list[len(self.paint_list)-1]])

        for point in self.paint_list:
            self.canvas.create_oval(point[0] - 1, point[1] - 1, point[0] + 1, point[1] + 1, fill="orange", outline="")

    def normalize(self, position):
        return [position[0], self.canvas.winfo_width() - position[1]]