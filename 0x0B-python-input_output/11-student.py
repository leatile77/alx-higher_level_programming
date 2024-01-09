#!/usr/bin/python3
"""Defines a class Student"""
class Student:
    """Represents a student."""
    def __init__(self, first_name, last_name, age):
        """Initialise student.
        Args:
            first_name (str): First name of student
            last_name (str): Last name of student
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets dict representation of Student class.
        Args:
            attrs (list): Attribute to represent
        Return:
              dictionary representation of student
        """
        if (type(attrs) == list and all(type(elem) == str for elem in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Method that replaces all attributes of Student instance.
        Args:
        json (dict): key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
