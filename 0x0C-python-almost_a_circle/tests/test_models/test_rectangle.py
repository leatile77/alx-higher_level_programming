#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle_init(unittest.TestCase):
    """Unittests for instantiation of Rectangle class"""
    def test_rect_is_base(self):
        self.assertIsInstance(Rectangle(3, 6), Base)

    def test_rect_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_rect_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(3)

    def test_rect_two_to_four_args(self):
        r1 = Rectangle(7, 8)
        r2 = Rectangle(9, 4, 3)
        r3 = Rectangle(5, 2, 8, 1)
        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r2.id, r3.id - 1)

    def test_rect_five_args(self):
        r1 = Rectangle(5, 2, 8, 1, 6)
        self.assertEqual(6, r1.id)

    def test_rect_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 4, 2, 8, 9, 1)

    def test_rect_priv_width(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(6, 9, 7, 2, 8).__width)

    def test_rect_priv_height(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(6, 9, 7, 2, 8).__height)

    def test_rect_priv_x(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(6, 9, 7, 2, 8).__x)

    def test_rect_priv_y(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(6, 9, 7, 2, 8).__y)

    def test_rect_width_getter(self):
        r1 = Rectangle(6, 9, 7, 2, 8)
        self.assertEqual(6, r1.width)

    def test_rect_width_setter(self):
        r1 = Rectangle(6, 9, 7, 2, 8)
        r1.width = 4
        self.assertEqual(4, r1.width)

    def test_rect_height_getter(self):
        r1 = Rectangle(6, 9, 7, 2, 8)
        self.assertEqual(9, r1.height)

    def test_rect_height_setter(self):
        r1 = Rectangle(6, 9, 7, 2, 8)
        r1.height = 6
        self.assertEqual(6, r1.height)

    def test_rect_x_getter(self):
        r1 = Rectangle(6, 9, 7, 2, 8)
        self.assertEqual(7, r1.x)

    def test_rect_x_setter(self):
        r1 = Rectangle(6, 9, 7, 2, 8)
        r1.x = 6
        self.assertEqual(6, r1.x)

    def test_rect_y_getter(self):
        r1 = Rectangle(6, 9, 7, 2, 8)
        self.assertEqual(2, r1.y)

    def test_rect_y_setter(self):
        r1 = Rectangle(6, 9, 7, 2, 8)
        r1.y = 3
        self.assertEqual(3, r1.y)


class TestRectangle_width(unittest.TestCase):
    """Unittests for width atteibute from Rectangle class"""
    def test_rect_width_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_rect_width_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hey", 2)

    def test_rect_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.76, 2)

    def test_rect_width_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(False, 2)

    def test_rect_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 2)

    def test_rect_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 2)

    def test_rect_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 2)

    def test_rect_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"one": 1,"two": 2}, 2)

    def test_rect_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2)

    def test_rect_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)


class TestRectangle_height(unittest.TestCase):
    """Unittests for height attribute from Rectangle class."""
    def test_rect_height_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None)

    def test_rect_height_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(3, "Hey")

    def test_rect_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 3.76)

    def test_rect_height_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, False)

    def test_rect_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, [1, 2, 3])
            
    def test_rect_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(7, (1, 2, 3))

    def test_rect_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, {1, 2, 3})

    def test_rect_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, {"one": 1,"two": 2})

    def test_rect_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -2)

    def test_rect_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests for x attribute from Rectangle class."""
    def test_rect_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, None)

    def test_rect_x_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 3, "Hey")

    def test_rect_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 1, 3.76)

    def test_rect_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(7, 5, True)
            
    def test_rect_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(8, 5, [1, 2, 3])

    def test_rect_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 7, (1, 2, 3))

    def test_rect_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 1, {1, 2, 3})

    def test_rect_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 9, {"one": 1,"two": 2})

    def test_rect_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(9, 1, -2)


class TestRectangle_y(unittest.TestCase):
    """Unittests for y attribute from Rectangle class."""
    def test_rect_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 5, 2, None)

    def test_rect_y_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(7, 3, 6, "Hey")

    def test_rect_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 4, 1, 3.76)

    def test_rect_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 2, 5, False)

    def test_rect_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(4, 2, 5, [1, 2, 3])

    def test_rect_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(5, 6, 7, (1, 2, 3))

    def test_rect_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 2, 3, {1, 2, 3})

    def test_rect_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(3, 8, 9, {"one": 1,"two": 2})

    def test_rect_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(3, 2, 1, -2)


class TestRectangle_area(unittest.TestCase):
    """Unittests of area method from REctangle class."""
    def test_rect_area_small(self):
        r1 = Rectangle(5, 3, 0, 0, 0)
        self.assertEqual(15, r1.area())

    def test_rect_area_big(self):
        r1 = Rectangle(200, 100, 0, 0, 0)
        self.assertEqual(20000, r1.area())

    def test_rect_area_changed_size(self):
        r1 = Rectangle(5, 3, 0, 0, 0)
        r1.width = 10
        r1.height = 2
        self.assertEqual(20, r1.area())

    def test_rect_area_passing_args(self):
        r1 = Rectangle(2, 20, 0, 1, 0)
        with self.assertRaises(TypeError):
            r1.area(2)

if __name__ == "__main__":
    unittest.main()
