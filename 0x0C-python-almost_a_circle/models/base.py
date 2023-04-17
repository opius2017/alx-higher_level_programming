#!/usr/bin/python3
import json
import csv
import turtle


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, mode="w", encoding="utf-8") as myFile:
            myFile.write(cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as myFile:
                content = myFile.read()
                json_list = cls.from_json_string(content)
                return [cls.create(**d) for d in json_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="") as myFile:
            writer = csv.writer(myFile)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    row = [obj.id, obj.width, obj.height, obj.x, obj.y]
                elif cls.__name__ == "Square":
                    row = [obj.id, obj.size, obj.x, obj.y]
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", newline="") as myFile:
                reader = csv.reader(myFile)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        dictionary = {
                                "id": int(row[0]), "width": int(row[1]),
                                "height": int(row[2]), "x": int(row[3]),
                                "y": int(row[4])}
                    elif cls.__name__ == "Square":
                        dictionary = {
                                "id": int(row[0]), "size": int(row[1]),
                                "x": int(row[2]), "y": int(row[3])}
                    instance = cls.create(**dictionary)
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        t = turtle.Turtle()
        t.speed(0)
        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            for i in range(2):
                t.forward(rect.width)
                t.left(90)
                t.forward(rect.height)
                t.left(90)
                for square in list_squares:
                    t.penup()
                    t.goto(square.x, square.y)
                    t.pendown()
                    for i in range(4):
                        t.forward(square.size)
                        t.left(90)
                        turtle.done()
