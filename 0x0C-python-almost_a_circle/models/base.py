#!/usr/bin/python3

import json
class Base:
    __nb_objects = 0
    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
"""
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return (json.dumps(list_dictionaries))
        

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)

        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dc_list = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(dc_list))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary:
            if cls.__name__ == "Rectangle":
                updated = cls(1, 1)
            else:
                updated = cls(1)
            updated.update(**dictionary)
            return updated

    
    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as jsonfile:
                from_file = jsonfile.read()
                if not from_file.strip():
                    return []
                dct_list = Base.from_json_string(from_file)
                return [cls.create(**dct) for dct in dct_list]
        except FileNotFoundError:
            return []
"""
