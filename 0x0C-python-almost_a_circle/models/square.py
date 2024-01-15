#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
        
    def to_dictionary(self):
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
