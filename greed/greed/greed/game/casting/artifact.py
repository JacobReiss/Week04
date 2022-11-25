from game.shared.point import Point
from game.casting.actor import Actor

from game.shared.color import Color
import random

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    """The message banner artifact. 
    
    The responsibility of Artifact is to display the message banner at the top.

    Attributes:
        Actor (Actor): The Actor class
        _message (String): The message to display
    """
    
    def __init__(self):
        super().__init__()
        self._message = ""
        
    def get_message(self):
        return self._message
    
    def set_message(self, message):
        self._message = message
        
    def get_point_value(self):
        points = 0
        
        if (self.get_text() == "*"):
            points = 1
        else:
            points = -1
            
        return points
        
    def move_down(self):
        # Moves the artifact down the screen to represent flying past it in space.
        y = self._position.get_y() + 5
        
        if y == 600:
            y = 0
        
        self._position = Point(self._position.get_x(), y)
        
    def refresh(self):
        # Changes the position and color of the artifact, resetting it as if it were a new artifact.
        x = random.randint(1, 59)
        # y = random.randint(1, ROWS - 1)
        position = Point(x, 0)
        position = position.scale(15)
        self.set_position(position)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.set_color(Color(r, g, b))