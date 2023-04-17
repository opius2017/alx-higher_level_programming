#!/usr/bin/python3
"""Module defining Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square object"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return a string representation of the Square"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get the size of the Square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the Square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the Square"""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
