#!/usr/bin/python3
"""Recangle module"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class representation"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        self.val_vald("width", width, False)
        self.val_vald("height", height, False)
        if x != 0:
            self.val_vald("x", x)
        if y != 0:
            self.val_vald("y", y)

    @property
    def width(self):
        """get the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of the width"""
        self.val_vald("width", value, False)
        self.__width = value

    @property
    def height(self):
        """get the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of the height"""
        self.val_vald("height", value, False)
        self.__height = value

    @property
    def x(self):
        """get the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value of x"""
        self.val_vald("x", value)
        self.__x = value

    @property
    def y(self):
        """get the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value of y"""
        self.val_vald("y", value)
        self.__y = value

    def val_vald(self, name, value, x_y=True):
        """method to validate the value entered"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if not x_y and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if x_y and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    def area(self):
        """Method for calculating the area"""
        return self.width * self.height

    def display(self):
        """method for displaying the rectangle by symbol #"""
        row = 1
        print("\n" * self.y, end="")
        while row <= self.height:
            print(" " * self.x, end="")
            print("#" * self.width)
            row += 1

    def __str__(self):
        """returns user friendly info about the rectangle"""
        return "[{}] ({}) {}/{} - {}/{}"\
            .format(type(self).__name__, self.id, self.x,
                    self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """method to update the values of the rectangele
        instance based on args"""
        if args:
            if len(args) >= 0:
                self.id = args[0]
            if len(args) >= 1:
                self.width = args[1]
            if len(args) >= 2:
                self.height = args[2]
            if len(args) >= 3:
                self.x = args[3]
            if len(args) >= 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary reperesentation of a rectangle instance"""
        return {"id": self.id, "width": self.__width, "height": self.__height,
                "x": self.__x, "y": self.__y}
