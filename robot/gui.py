from tkinter import *
from robot.robot_drawer import *
from time import sleep


class GUI:

    def __init__(self, robot):

        self.monitor_height = None
        self.monitor_width = None

        # main window configuration
        self.window = Tk()
        self.configure_window()

        # frame configurations
        self.frame_top = None
        self.configure_frames()

        self.canvas = None
        self.configure_widgets()

        self.robotDrawer = RobotDrawer(robot)
        self.robotDrawer.set_canvas(self.canvas)

    # @function_task:
    # This function configures the root tk window object
    def configure_window(self):
        self.window.pack_propagate(False)
        self.window.title("CirclerRobot")
        self.window.attributes('-fullscreen', False)
        self.window.update()
        self.monitor_height = 800
        self.monitor_width = 800
        self.window.geometry(str(self.monitor_width) + "x" + str(self.monitor_height) + "+0+0")
        print(str(self.monitor_width) + "x" + str(self.monitor_height) + "+0+0")
        self.window.resizable(False, False)  # x dimension resizing false, y dimension resizing false

    # This function creates frame objects and makes their configurations
    # And create a layout by placing them into root window
    def configure_frames(self):

        self.frame_top = Frame(
            self.window,
            bg="gold",
            height=self.monitor_height,
            width=self.monitor_width)
        self.frame_top.pack_propagate(False)
        self.frame_top.grid(row=0, column=0)

    # @function_task:
    # This function creates widget objects and makes their configurations
    def configure_widgets(self):

        # map screen
        self.canvas = Canvas(
            self.frame_top,
            bg="black",
            borderwidth=0,
            highlightthickness=0,
            height=self.monitor_height,
            width=self.monitor_width)
        self.canvas.place(in_=self.frame_top, anchor="c", relx=.5, rely=.5)

    # refresh function updates canvas in every 1 ms
    def refresh(self):
        self.robotDrawer.refresh()
        self.window.after(1, self.refresh)

    def start(self):
        self.refresh()
        self.window.mainloop()

