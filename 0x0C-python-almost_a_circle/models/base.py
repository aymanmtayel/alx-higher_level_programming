#!/usr/bin/python3
"""Class Base Module"""
import json
import csv
import turtle


class Base:
    """A base class counting the number of instances"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON representation of list_dictionaries"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save a json object to a file"""
        if list_objs is not None:
            list_objs = [objects.to_dictionary() for objects in list_objs]
        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """returns a json string after loading"""
        if json_string is None or not json_string:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all the attributes already set"""
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances from a file"""
        fname = f"{cls.__name__}.json"
        try:
            with open(fname, "r", encoding="utf-8") as file:
                reads = file.read()
                classjson = cls.from_json_string(reads)
                instances = [cls.create(**items) for items in classjson]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes into CSV file"""
        fname = f"{cls.__name__}.csv"
        with open(fname, "w", newline="", encoding="utf-8") as file:
            write = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    write.writerow([obj.id, obj.width,
                                    obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    write.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """load instances from a csv file"""
        fname = f"{cls.__name__}.csv"
        try:
            with open(fname, "r", newline="", encoding="utf-8") as file:
                read = csv.reader(file)
                instances = []
                for line in read:
                    if cls.__name__ == "Rectangle":
                        instances.append(cls.create(id=int(line[0]),
                                                    width=int(line[1]),
                                                    height=int(line[2]),
                                                    x=int(line[3]),
                                                    y=int(line[4])))
                    elif cls.__name__ == "Square":
                        instances.append(cls.create(id=int(line[0]),
                                                    size=int(line[1]),
                                                    x=int(line[2]),
                                                    y=int(line[3])))
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        from random import randrange
        turtle.Screen().colormode(255)
        for obj in list_rectangles + list_squares:
            instance = turtle.Turtle()
            instance.color((randrange(255), randrange(255), randrange(255)))
            instance.pensize(0)
            instance.penup()
            instance.pendown()
            instance.setpos((obj.x + instance.pos()[0],
                            obj.y - instance.pos()[1]))
            instance.pensize(4)
            instance.forward(obj.width)
            instance.left(90)
            instance.forward(obj.height)
            instance.left(90)
            instance.forward(obj.width)
            instance.left(90)
            instance.forward(obj.height)
            instance.left(90)
            instance.end_fill()
        turtle.mainloop()
