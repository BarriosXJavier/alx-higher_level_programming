#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square class.

        Args:
            size (int): Size of the square.
            x (int, optional): x-coordinate of the square (default is 0).
            y (int, optional): y-coordinate of the square (default is 0).
            id (int, optional): Identifier for the square (default is None).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def to_dictionary(self):
        """Return the dictionary representation of the Square instance."""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

