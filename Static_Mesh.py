
# Paddle width, usded also for ball size
PADDLE_WIDTH = 50

class Paddle:
    pass

class Ball:
    # Ball x and y positions as class variable since there's going to be only one instance of this class
    _pos_x = 0
    _pos_y = 0
    # Balls vertical and horizontal velocity, again as class variable
    velocity_v = 10
    velocity_h = 10

    def __init__(self) -> None:
        # Set the size of ball
        self.width = PADDLE_WIDTH
        self.heigth = PADDLE_WIDTH
    
    def Update(self, delta_time :float):
        # Update balls position using delta time
        self._pos_x += self.velocity_h * delta_time
        self._pos_y = self.velocity_v * delta_time