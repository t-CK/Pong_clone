from Graphics import *
from Static_Mesh import *
from pygame import time

class Game_Mechanics:
    # Class is going to be static
    __wnd :Window
    __p1 :Paddle
    __p2 :Paddle
    __ball :Ball
    __delta_time :float
    __prev_tick = 0
    __is_running :bool  # A boolean variable to keep track of game running status

    # Initialize the game
    def __init__(self) -> None:
        # Create the window
        self.__wnd = Window()

        # Setup clock to keep track of ticks
        self.__timer = time.Clock()

        # Get number of players from user
        
        # Create static meshes
        self.__p1 = Paddle(1)
        # Paddle2
        self.__ball = Ball()
        # Set __is_running to True
        self.__is_running = True

    
    def Get_Input(self):
        pass

    def Calculate_Delta_Time(self) -> None:
        """Calculates delta time and saves it into class variable"""
        # Set first tick to 0
       # if self.__prev_tick == None:
       #     self.__prev_tick = 0

        self.__delta_time = (time.get_ticks() - self.__prev_tick) / 1000.0
        

    def Game_Loop(self):
        while self.__is_running:
            self.Calculate_Delta_Time()
            print(self.__delta_time)
            self.Get_Input()
            self.__ball.Update()
            self.__wnd.Render()
            self.__prev_tick = time.get_ticks()

