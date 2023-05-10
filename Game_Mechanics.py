from Graphics import *
from Static_Mesh import *

class Game_Mechanics:
    # Class is going to be static
    __wnd :Window
    __p1 :Paddle
    __p2 :Paddle
    __ball :Ball
    __delta_time :float
    __is_running :bool  # A boolean variable to keep track of game running status

    # Initialize the game
    def __init__(self) -> None:
        # Create the window
        self.__wnd = Window()

        # Get number of players from user
        
        # Create static meshes
        self.__p1 = Paddle()
        # Paddle2
        self.__ball = Ball()

    
    def Get_Input(self):
        pass

    def Game_Loop(self):
        while self.__is_running:
            # Calculate delta time
            self.Get_Input()
            self.__ball.Update()
            self.__wnd.Render()

