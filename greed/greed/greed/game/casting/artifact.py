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
        """Constructs a new Artifact
        """
        super().__init__()
        
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
        
    def refresh(self):
        """Resets the artifact after the Actor makes it diasppear.
        """
        x = random.randint(1, 59)
        position = Point(x, 0)
        position = position.scale(15)
        self.set_position(position)
        
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.set_color(Color(r, g, b))
            