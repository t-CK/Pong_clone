from pygame import display
from pygame import surface
from Static_Mesh import *

class Window:
    # Class member variables
    # Class is going to be static, so we can add everything as class variable
    __screen_width  :int
    __screen_heigth :int
    __wnd           :surface.Surface

    def __init__(self) -> None:
        # Initialize display module
        display.init()
        # Set the values and create the window
        self.__screen_width = 1080
        self.__screen_heigth = 750
        self.__wnd = display.set_mode((self.__screen_width, self.__screen_heigth))

    # Draw objects and render the window
    def Render(self, p1 :Paddle, p2 :Paddle, ball :Ball):
        # Clear the screen with blue
        self.__wnd.fill(color=(0, 0, 255))

        # Flip buffers
        display.flip()
