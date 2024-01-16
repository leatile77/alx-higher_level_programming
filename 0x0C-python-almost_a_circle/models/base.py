#!/usr/bin/python3

"""Defines a base class."""

import json
class Base:
    """Base model.
    private class attribute:
    __nb_objects (int): Number of instantiated bases.
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializes new base.
        Args:
        id (int): identity of new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON serialized list of dicts.
        Args:
        list_dictionaries (list): List of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return (json.dumps(list_dictionaries))
        

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON serialization of list of objects to a file.
        Args:
        list_objs (list): List of Base instances.
        """
        filename = "{}.json".format(cls.__name__)

        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dc_list = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(dc_list))

    @staticmethod
    def from_json_string(json_string):
        """Returns deserialization of a JSON string.
        Args:
        json_string (str): JSON representation of a list of dicts
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantiated from a dict.
        Args:
        **dictionary (dict): k/v pairs of attributes.
        """
        if dictionary:
            if cls.__name__ == "Rectangle":
                updated = cls(1, 1)
            else:
                updated = cls(1)
            updated.update(**dictionary)
            return updated

    
    @classmethod
    def load_from_file(cls):
        """Returns a list of classes instantiated from a JSON file.
        Returns:
        if file not found - empty list
        else - a list of instantiated classes
        """
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
