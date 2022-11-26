from game.shared.point import Point
from game.casting.actor import Actor
from game.shared.color import Color

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
        y = self._position.get_y() + 10
        
        if y == 600:
            y = 0
        
        self._position = Point(self._position.get_x(), y)
        