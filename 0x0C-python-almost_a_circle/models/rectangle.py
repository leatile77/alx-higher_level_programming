#!/usr/bin/python3
"""Defines Rectangle class."""

from models.base import Base

class Rectangle(Base):
    """Represents rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize new rectangle.
        Args:
            width (int): Width of new Rectangle.
            height (int): Height of new Rectangle.
            x (int): x coordinate of Rectangle.
            y (int): y coordinate of Rectangle.
            id (int): identity of Rectangle.
        Raises:
            TypeError: if width, height, x or y is not type int.
            ValueError: if width or height <= 0.
            ValueError: if x or y < 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get/set width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) != int:
            raise TypeError("width must be an integer")
        if val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """get/set height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) != int:
            raise TypeError("height must be an integer")
        if val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """get/set x coordinate of Rectangle."""
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) != int:
            raise TypeError("x must be an integer")
        if val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """get/set y coordinate of Rectangle."""
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """Returns area of rectangle."""
        return self.width * self.height

    def display(self):
        """Print Rectangle using '#' character."""
        for verti in range(self.y):
            print("")

        for i in range(self.height):
            for hori in range(self.x):
                print(" ", end='')

            for j in range(self.width):
                print("#", end='')
            print("")
        
    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        Args:
            *args (ints): New values:
               1st argument should be the id attribute
               2nd argument should be the width attribute
               3rd argument should be the height attribute
               4th argument should be the x attribute
               5th argument should be the y attribute
          
            **kwargs (dict): new pairs of attributes.
        """
        if args and len(args) != 0:
            k = 0
            for arg in args:
                if k == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif k == 1:
                    self.width = arg
                elif k == 2:
                    self.height = arg
                elif k == 3:
                    self.x = arg
                elif k == 4:
                    self.y = arg
                k += 1

        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "id":
                    if val is None:
                         self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = val

                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val

    def to_dictionary(self):
        """Returns dictionary representation of Rectangle.""" 
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
