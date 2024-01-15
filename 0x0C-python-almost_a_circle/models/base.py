#!/usr/bin/python3

import json
import csv
import turtle

class Base:
    """Base class for managing id attribute in other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): List of instances inheriting from Base.
        """
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.json"
        with open(filename, 'w') as file:
            file.write(cls.to_json_string([obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list of dictionaries represented by json_string.

        Args:
            json_string (str): JSON string representing a list of dictionaries.

        Returns:
            list: List of dictionaries.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set.

        Args:
            **dictionary: Dictionary representing attributes.

        Returns:
            Base: Instance with attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            raise NotImplementedError("create method not implemented for this class")

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances loaded from a file.

        Returns:
            list: List of instances.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                instances = [cls.create(**dictionary) for dictionary in dictionaries]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize instances to CSV format and write to a file.

        Args:
            list_objs (list): List of instances inheriting from Base.
        """
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                else:
                    raise NotImplementedError("save_to_file_csv method not implemented for this class")
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize instances from a CSV file.

        Returns:
            list: List of instances.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    else:
                        raise NotImplementedError("load_from_file_csv method not implemented for this class")
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Open a window and draw all the Rectangles and Squares.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.
        """
        # Create a Turtle screen
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.bgcolor("white")

        # Create a Turtle object
        artist = turtle.Turtle()
        artist.speed(2)  # Set the drawing speed

        # Draw Rectangles
        for rectangle in list_rectangles:
            artist.penup()
            artist.goto(rectangle.x, rectangle.y)
            artist.pendown()
            artist.color("blue")  # Set color for Rectangles
            for _ in range(2):
                artist.forward(rectangle.width)
                artist.left(90)
                artist.forward(rectangle.height)
                artist.left(90)

        # Draw Squares
        for square in list_squares:
            artist.penup()
            artist.goto(square.x, square.y)
            artist.pendown()
            artist.color("red")  # Set color for Squares
            for _ in range(4):
                artist.forward(square.size)
                artist.left(90)

        # Close the window on click
        screen.exitonclick()

 Base.draw(list_rectangles, list_squares)

