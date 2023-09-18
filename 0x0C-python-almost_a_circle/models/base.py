#!/usr/bin/python3
import json
import csv
import turtle


class Base:
    """
    Base class for managing common attributes and methods of other classes.

    Attributes:
        __nb_objects (int): A private class variable to keep track of the
        number of Base instances created.

    Methods:
        __init__(self, id=None):
            Initializes a Base instance with a unique ID or auto-generates one
            if id is None.
        to_json_string(list_dictionaries):
            Static method to convert a list of dictionaries to a JSON string.
        save_to_file(cls, list_objs):
            Class method to save a list of objects to a JSON file.
        from_json_string(json_string):
            Static method to convert a JSON string to a list of dictionaries.
        create(cls, **dictionary):
            Class method to create an instance based on a dictionary of
            attributes.
        load_from_file(cls):
            Class method to load objects from a JSON file and create instances.
        save_to_file_csv(cls, list_objs):
            Class method to save a list of objects to a CSV file.
        load_from_file_csv(cls):
            Class method to load objects from a CSV file and create instances.
        draw(list_rectangles, list_squares):
            Static method to draw rectangles and squares using the Turtle
            graphics library.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with a unique ID or auto-generates one if
        id is None.

        Args:
            id (int, optional): The ID of the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method to convert a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries to be converted.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method to save a list of objects to a JSON file.

        Args:
            cls (class): The class calling this method.
            list_objs (list): A list of objects to be saved.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [y.to_dictionary() for y in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Static method to convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string to be converted.

        Returns:
            list: A list of dictionaries parsed from the JSON string.
        """
        if json_string is None or json_string == []:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method to create an instance based on a dictionary of attributes.

        Args:
            cls (class): The class calling this method.
            **dictionary: Keyword arguments representing the attributes of the
            instance to be created.

        Returns:
            obj: An instance of the class with attributes initialized from the
            dictionary.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """
        Class method to load objects from a JSON file and create instances.

        Args:
            cls (class): The class calling this method.

        Returns:
            list: A list of instances created from the data in the JSON file.
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Class method to save a list of objects to a CSV file.

        Args:
            cls (class): The class calling this method.
            list_objs (list): A list of objects to be saved.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Class method to load objects from a CSV file and create instances.

        Args:
            cls (class): The class calling this method.

        Returns:
            list: A list of instances created from the data in the CSV file.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [
                    dict([k, int(v)] for k, v in d.items()) for d in list_dicts
                ]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Static method to draw rectangles and squares using the Turtle graphics
        library.

        Args:
            list_rectangles (list): A list of Rectangle instances to be drawn.
            list_squares (list): A list of Square instances to be drawn.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("white")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
