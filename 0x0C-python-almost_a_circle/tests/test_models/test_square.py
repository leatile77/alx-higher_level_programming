#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare_init(unittest.TestCase):
    """Unittests for instantiation of Square class"""
    def test_sqr_is_base(self):
        self.assertIsInstance(Square(3), Base)

    def test_sqr_is_rect(self):
        self.assertIsInstance(Square(3), Rectangle)

    def test_sqr_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_sqr_one_arg(self):
        s1 = Square(9)
        s2 = Square(8)
        self.assertEqual(s1.id, s2.id - 1)

    def test_sqr_two_to_three_args(self):
        s1 = Square(7, 8)
        s2 = Square(9, 4, 3)
        self.assertEqual(s1.id, s2.id - 1)
        

    def test_sqr_four_args(self):
        s1 = Square(2, 8, 1, 6)
        self.assertEqual(6, s1.id)

    def test_sqr_more_than_four_args(self):
        with self.assertRaises(TypeError):
            Square(5, 4, 2, 8, 9)

    def test_sqr_priv_size(self):
        with self.assertRaises(AttributeError):
            print(Square(6, 9, 7, 2).__size)

    def test_sqr_size_getter(self):
        self.assertEqual(6, Square(6, 2, 3, 1).size)

    def test_sqr_size_setter(self):
        s1 = Square(2, 4, 6, 8)
        s1.size = 3
        self.assertEqual(3, s1.size)

    def test_sqr_width_setter(self):
        s1 = Square(9, 7, 2, 8)
        s1.width = 4
        self.assertEqual(4, s1.width)

    def test_sqr_height_setter(self):
        s1 = Square(9, 7, 2, 8)
        s1.height = 6
        self.assertEqual(6, s1.height)

    def test_sqr_x_getter(self):
        s1 = Square(6)
        self.assertEqual(0, s1.x)

    def test_sqr_y_getter(self):
        s1 = Square(7)
        self.assertEqual(0, s1.y)


class TestSquare_size(unittest.TestCase):
    """Unittests for size attribute from Square class"""
    def test_sqr_size_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_sqr_size_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("Hey")

    def test_sqr_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(3.76, 9)

    def test_sqr_size_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(False, 1, 4)

    def test_sqr_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3], 2)

    def test_sqr_size_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2)

    def test_sqr_size_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3})

    def test_sqr_size_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"one": 1,"two": 2}, 7)

    def test_sqr_size_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_sqr_size_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """Unittests for x attribute from Square class."""
    def test_sqr_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, None)

    def test_sqr_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(3, "Hey")

    def test_sqr_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 3.76)

    def test_sqr_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, False)

    def test_sqr_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(5, [1, 2, 3])
            
    def test_sqr_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(7, (1, 2, 3))

    def test_sqr_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_sqr_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(9, {"one": 1,"two": 2})

    def test_sqr_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2)


class TestSquare_y(unittest.TestCase):
    """Unittests for y attribute from Square class."""
    def test_sqr_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, None)

    def test_sqr_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, "Hey")

    def test_sqr_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 1, 3.76)

    def test_sqr_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(7, 5, True)
            
    def test_sqr_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(8, 5, [1, 2, 3])

    def test_sqr_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(9, 7, (1, 2, 3))

    def test_sqr_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 1, {1, 2, 3})

    def test_sqr_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(3, 9, {"one": 1,"two": 2})

    def test_sqr_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(9, 1, -2)


class TestSquare_area(unittest.TestCase):
    """Unittests of area method from Square class."""
    def test_sqr_area_small(self):
        s1 = Square(5, 3, 0, 0)
        self.assertEqual(25, s1.area())

    def test_sqr_area_big(self):
        s1 = Square(200, 100, 0, 0)
        self.assertEqual(40000, s1.area())

    def test_sqr_area_changed_size(self):
        s1 = Square(5, 3, 0, 0)
        s1.size = 10
        self.assertEqual(100, s1.area())

    def test_sqr_area_passing_args(self):
        s1 = Square(2, 20, 0, 1)
        with self.assertRaises(TypeError):
            s1.area(2)

if __name__ == "__main__":
    unittest.main()
