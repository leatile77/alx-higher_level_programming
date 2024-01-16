#!/usr/bin/python3
"""DEfines a Square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a Square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square (rectangle with equal sides).
        Args:
        size (int): size of a new Square
        x (int): x coordinate of square.
        y (int): y coordinate of square.
        id (int): identity of new square.
        """
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        """Get/set size of square."""
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """Update square.
        Args:
        *args (ints): New attributes.
        - 1st argument should be the id attribute
        - 2nd argument should be the size attribute
        - 3rd argument should be the x attribute
        - 4th argument should be the y attribute
        
        **kwargs (dict): key/value attributes.
        """
        if args and len(args) != 0:
            s = 0
            for arg in args:
                if s == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg

                elif s == 1:
                    self.size = arg
                elif s == 2:
                    self.x = arg
                elif s == 3:
                    self.y = arg
                s += 1

        elif kwargs and len(kwargs) != 0:
            for ky, vl in kwargs.items():
                if ky == "id":
                    if vl is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = vl

                elif ky == "size":
                    self.size = vl
                elif ky == "x":
                    self.x = vl
                elif ky == "y":
                    self.y = vl
                

    def __str__(self):
        """Returns print() and str() representation of Square.""" 
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
        
    def to_dictionary(self):
        """Returns dictionary representation of Square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
