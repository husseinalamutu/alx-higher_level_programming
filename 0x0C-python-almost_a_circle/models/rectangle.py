#!/usr/bin/python3
"""Defines a Rectangle model class."""
from models.base import Base
from turtle import width


class Rectangle(Base):
    """Represents a rectangle class that inherits from the base class.
    Args:
        Base(model): the model that was inherited.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructs the rectangle attribute

        Keyword:
            super(): Allows the "rectangle class" to inherit the init()
            property of it's parent class (base)

        Args:
            width(int): the width of the rectangle.
            height(int): the height of the rectangle.
            x(int): the horizontal position of the recatngle.
            y(int): the vertical position of the rectangle.
            id(int): the identity of the recytangle.
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets width(privately) of the rectangle"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets the width(privately) of the rectangle"""
        if value not in [int]:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height(privately) of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height(privately) of the rectangle"""
        if value not in [int]:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value    

    @property
    def x(self):
        """Gets the horizontal position(privately) of the rectangle"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """Sets the horizontal position(privately) of the rectangle"""
        if value not in [int]:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError ("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the vertical position(privately) of the rectangle"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Sets the vertical position(privately) of the rectangle"""
        if value not in [int]:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError ("y must be >= 0")
        self.__y = value

    def area(self):
        """public method that returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Public method that prints in "stdout" the Rectangle 
        instance with the character #
        """
        print("\n" * self.y, end="")
        print((" " * self.x, + "#" * self.__width + "\n") * self.__height, end="\n")

    def __str__(self):
        """String representation of the rectangle class"""
        str_res = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.__width, self.__height)
        return str_res

    def update(self, *args, **kwargs):
        """Public method that assigns an argument to each attribute
        
        Args:
            *args: assigns no-keyword argument
            **kwargs: assigns key-worded arguments
        """
        if not args and not kwargs:
            return None
        if args is not None:
            attributes = ["id", "width", "height", "x", "y"]
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for k, v in enumerate(kwargs):
                if hasattr(self , k):
                    setattr(self, k, v) 

    def to_dictionary(self):
        """Public method that returns the dictionary representation of the rectangle class"""
        
        _map = {}
        for key, value in self.__dict__.item():
            if key.startswith("_"):
                _map[key.split("__")[-1]] = value
            else:
                _map = value
        return _map
        