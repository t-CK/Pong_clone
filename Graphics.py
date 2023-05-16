from multipledispatch import dispatch
from pygame import display
from pygame import surface
from pygame import draw
from Static_Mesh import *

class Window:
    # Class member variables
    # Class is going to be static, so we can add everything as class variable
    __screen_width  :int
    __screen_heigth :int
    __wnd           :surface.Surface
    __mesh_color = (255, 255, 255)

    def __init__(self) -> None:
        # Initialize display module
        display.init()
        # Set the values and create the window
        self.__screen_width = 1080
        self.__screen_heigth = 750
        self.__wnd = display.set_mode((self.__screen_width, self.__screen_heigth))

    def Get_Heigth(self) -> int:
        return self.__screen_heigth
    def Get_Width(self) -> int:
        return self.__screen_width

    # Draw objects and render the window
    # Overload for 2 players
    @dispatch(Ball, Paddle, Paddle)
    def Render(self, ball :Ball, p1 :Paddle, p2 :Paddle):
        pass

    # Draw objects and render the window
    # Overload for 1 player
    @dispatch(Ball, Paddle)
    def Render(self, ball :Ball, p1 :Paddle):
        # Clear the screen with blue
        self.__wnd.fill(color=(0, 0, 255))

        # Draw walls
        w_top = draw.rect(self.__wnd, color=self.__mesh_color, rect=(0, 15, self.__screen_width -15, 20))
        w_bottom = draw.rect(self.__wnd, color=self.__mesh_color, rect=(0, self.__screen_heigth - 35, self.__screen_width -15, 20))
        w_back = draw.rect(self.__wnd, color=self.__mesh_color, rect=(self.__screen_width -35, 20, 20, self.__screen_heigth - 35)) # Rear wall for 1p game

        # Draw the ball
        ball_mesh = draw.rect(self.__wnd, color=(255, 255, 255), rect=(ball._pos_x, ball._pos_y, PADDLE_WIDTH, PADDLE_WIDTH))

        # Update display
        display.update()
        # Flip buffers
        display.flip()
