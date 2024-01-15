#!/usr/bin/python3

import os
import unittest

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase_Init(unittest.TestCase):
    """Unittests for init method of Base class"""
    def test_three_no_args(self):
        bs1 = Base()
        bs2 = Base()
        bs3 = Base()
        self.assertEqual(bs1.id, bs2.id - 1)
        self.assertEqual(bs2.id, bs3.id - 1)
        self.assertEqual(bs1.id, bs3.id - 2)

    def test_id_as_None(self):
        bs1 = Base()
        bs2 = Base()
        self.assertEqual(bs1.id, bs2.id - 1)

    def test_id_specified(self):
        bs1 = Base(6)
        self.assertEqual(6, bs1.id)

    def test_id_before_and_after_specified_id(self):
        bs1 = Base()
        bs2 = Base(9)
        bs3 = Base()
        self.assertEqual(bs1.id, bs3.id - 1)

    def test_reassign_id(self):
        bs1 = Base(8)
        bs1.id = 11
        self.assertEqual(11, bs1.id)

    def test_nb_if_given_id(self):
        with self.assertRaises(AttributeError):
            print(Base(7).__nb_instances)

    def test_id_bool(self):
        self.assertEqual(True, Base(True).id)

    def test_id_string(self):
        self.assertEqual("Hey", Base("Hey").id)

    def test_id_float(self):
        self.assertEqual(9.7, Base(9.7).id)

    def test_id_list(self):
        self.assertEqual([1, 2], Base([1, 2]).id)

    def test_id_tuple(self):
        self.assertEqual((3, 4), Base((3, 4)).id)

    def test_id_set(self):
        self.assertEqual({5, 6}, Base({5, 6}).id)

    def test_id_dict(self):
        self.assertEqual({"one": 1, "two": 2}, Base({"one": 1, "two": 2}).id)

    def test_id_inf(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_extra_args(self):
        with self.assertRaises(TypeError):
            Base(7, 8)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for to_json_string method from Base class"""
    def test_json_rect_type(self):
        rec = Rectangle(8, 6, 2, 3, 3)
        self.assertEqual(str, type(Base.to_json_string([rec.to_dictionary()])))

    def test_json_square_type(self):
        sq = Square(6, 2, 3, 3)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_json_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_json_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_json_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_json_extra_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 3)


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for save_to_file method from Base class"""
    def test_save_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_none_as_arg(self):
         Square.save_to_file(None)
         with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_extra_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 9)


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for from_json_file method from Base class"""
    def test_from_json_type(self):
        inpt = [{"id": 2, "height": 8, "width": 7}]
        inp_json = Rectangle.to_json_string(inpt)
        outpt = Rectangle.from_json_string(inp_json)
        self.assertEqual(list, type(outpt))

    def test_from_json_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_extra_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 4)

    def test_from_json_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_None_as_arg(self):
        self.assertEqual([], Base.from_json_string(None))

class TestBase_create(unittest.TestCase):
    """Unittests for create method from Base class."""
    def test_create_rect(self):
        r1 = Rectangle(4, 6, 1, 2, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertEqual("[Rectangle] (8) 1/2 - 4/6", str(r2))

    def test_create_square(self):
        s1 = Square(4, 6, 1, 7)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertEqual("[Square] (7) 6/1 - 4", str(s2))

    def test_create_rect_is_rect(self):
        r1 = Rectangle(4, 6, 1, 2, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r1, r2)

    def test_create_rect_equals_rect(self):
        r1 = Rectangle(4, 6, 1, 2, 8)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)

    def test_create_squa_is_squa(self):
        s1 = Square(4, 6, 1, 2)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsNot(s1, s2)

    def test_create_squa_equals_squa(self):
        s1 = Square(4, 6, 1, 8)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertNotEqual(s1, s2)
        

class TestBase_load_from_file(unittest.TestCase):
    """Unittests for load_from_file method for Base class."""
    def test_load_first_rect(self):
        r1 = Rectangle(4, 6, 1, 2, 8)
        r2 = Rectangle(4, 5, 1, 1, 7)
        Rectangle.save_to_file([r1, r2])
        lst_out = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(lst_out[0]))

    def test_load_secnd_rect(self):
        r1 = Rectangle(4, 6, 1, 2, 8)
        r2 = Rectangle(4, 5, 1, 1, 7)
        Rectangle.save_to_file([r1, r2])
        lst_out = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(lst_out[1]))

    def test_load_rect_type(self):
        r1 = Rectangle(4, 6, 1, 2, 8)
        r2 = Rectangle(4, 5, 1, 1, 7)
        Rectangle.save_to_file([r1, r2])
        lst_out = Rectangle.load_from_file()
        self.assertTrue(all(type(ob) == Rectangle for ob in lst_out))

    def test_load_first_square(self):
        s1 = Square(6, 1, 2, 3)
        s2 = Square(4, 5, 1, 1)
        Square.save_to_file([s1, s2])
        lst_out = Square.load_from_file()
        self.assertEqual(str(s1), str(lst_out[0]))

    def test_load_secnd_square(self):
        s1 = Square(6, 1, 2, 3)
        s2 = Square(4, 5, 1, 1)
        Square.save_to_file([s1, s2])
        lst_out = Square.load_from_file()
        self.assertEqual(str(s2), str(lst_out[1]))

    def test_load_square_type(self):
        s1 = Square(6, 1, 2, 3)
        s2 = Square(4, 5, 1, 1)
        Square.save_to_file([s1, s2])
        lst_out = Square.load_from_file()
        self.assertTrue(all(type(ob) == Square for ob in lst_out))

    def test_load_extra_files(self):
        with self.assertRaises(TypeError):
            Base.load_from_file(True, 2)
        
if __name__ == "__main__":
    unittest.main()
