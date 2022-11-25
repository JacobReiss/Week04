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
    FRAME_RATE = 12
    MAX_X = 900
    MAX_Y = 600
    CELL_SIZE = 15
    FONT_SIZE = 15
    COLS = 60
    ROWS = 40
    CAPTION = "Greed"
    WHITE = Color(255, 255, 255)
    DEFAULT_ARTIFACTS = 40
    
    def __init__(self):
        """Constructs a new Artifact
        """
        super().__init__()
        self.FRAME_RATE = 12
        self.MAX_X = 900
        self.MAX_Y = 600
        self.CELL_SIZE = 15
        self.FONT_SIZE = 15
        self.COLS = 60
        self.ROWS = 40
        self.CAPTION = "Greed"
        self.WHITE = Color(255, 255, 255)
        self.DEFAULT_ARTIFACTS = 40
        
    def get_point_value(self):
        """Gets the point value depending on the object picked up

        Returns:
            points(int): The point value associated with the object type
        """
        points = 0
        
        if (self.get_text() == "*"):
            points = 1
            
        else:
            points = -1
            
        return points
        
    def move_down(self):
        """Moves the screen down to simulate the objects falling.
        """
        y = self._position.get_y() + 5
        
        if y == 600:
            y = 0
        
        self._position = Point(self._position.get_x(), y)
        