#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    """Rectangle class inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for Rectangle class.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): x-coordinate of the rectangle (default is 0).
            y (int, optional): y-coordinate of the rectangle (default is 0).
            id (int, optional): Identifier for the rectangle (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        self.__validate_integer(value, "width")
        self.__validate_positive(value, "width")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        self.__validate_integer(value, "height")
        self.__validate_positive(value, "height")
        self.__height = value

    @property
    def x(self):
        """Getter for x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x-coordinate."""
        self.__validate_integer(value, "x")
        self.__validate_non_negative(value, "x")
        self.__x = value

    @property
    def y(self):
        """Getter for y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y-coordinate."""
        self.__validate_integer(value, "y")
        self.__validate_non_negative(value, "y")
        self.__y = value

    def area(self):
        """Calculate and return the area of the Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance with '#' characters, taking into account x and y."""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Return a string representation of the Rectangle instance."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def to_dictionary(self):
        """Return the dictionary representation of the Rectangle instance."""
        return {'id': self.id, 'width': self.width, 'height': self.height, 'x': self.x, 'y': self.y}

    def __validate_integer(self, value, attribute_name):
        """Validate if the value is an integer."""
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer.")

    def __validate_positive(self, value, attribute_name):
        """Validate if the value is greater than 0."""
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0.")

    def __validate_non_negative(self, value, attribute_name):
        """Validate if the value is greater than or equal to 0."""
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0.")

