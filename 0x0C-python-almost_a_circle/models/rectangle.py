#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
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
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) != int:
            raise TypeError("y must be an integer")
        if val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        return self.width * self.height

    def display(self):
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
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}
