

# Paddle width, usded also for ball size
PADDLE_WIDTH = 20
PADDLE_HEIGTH = 100

class Paddle:
    def __init__(self, player_no :int, wnd_heigth :int) -> None:
        __movement_speed = 10
        # set the player number and paddle x-position accordingly
        self.__player_no = player_no
        if player_no == 1:
            self.__pos_x = 20   # Leave 20 pixel gap between paddle and window border
        else:
            pass # x_position for player 2 will be set to window width - (20 - PADDLE_WIDTH)

        # Set paddle Y pos to center of screen vertically
        self.__pos_y = (wnd_heigth / 2) - (PADDLE_HEIGTH / 2) 

    # Get the X position of paddle
    def Get_X(self) -> float:
        return self.__pos_x
    
    # Get the Y position of paddle
    def Get_Y(self) -> float:
        return self.__pos_y

    def Update(self, delta_time :float, input_value = 0):
        # Move the paddle
        self.__pos_x += self.__movement_speed * input_value * delta_time
        # Clamp to top/bottom of the play area

class Ball:
    # Ball x and y positions as class variable since there's going to be only one instance of this class
    _pos_x :int
    _pos_y :int
    # Balls vertical and horizontal velocity, again as class variable
    velocity_v = 10
    velocity_h = 10
    # Bounds for the ball
    __max_y :int
    __min_y :int

    def __init__(self, wnd_heigth :int, wnd_width :int) -> None:
        # Set position and size of the ball
        self._pos_x = (wnd_width / 2) - (PADDLE_WIDTH / 2)
        self._pos_y = (wnd_heigth / 2) - (PADDLE_WIDTH / 2)
        self.width = PADDLE_WIDTH
        self.heigth = PADDLE_WIDTH
        self.__max_y = wnd_heigth - PADDLE_WIDTH - 20 or self._pos_y <= 20
        self.__min_y = 20
    
    def Update(self, delta_time :float):
        # Clamp the ball into play area
        if self._pos_y >= self.__max_y:
            self.velocity_v *= -1
        
        
        # Update balls position using delta time
        self._pos_x += self.velocity_h * delta_time
        self._pos_y += self.velocity_v * delta_time

        

    # Reset the ball to default position
    def Reset(self):
        self._pos_x = 0
        self._pos_y = 0