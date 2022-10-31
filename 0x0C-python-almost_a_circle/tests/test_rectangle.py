#!/usr/bin/python3
"""
    Rectangle class unittest
"""
import unittest
import sys
import io
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """ class TestRectangle """

    def test_inheritance(self):
        """ test inheritance """
        self.assertTrue(issubclass(Rectangle, Base))

    def test_rect__args(self):
        """ test arguments """
        with self.assertRaises(TypeError):
            r = Rectangle()
        with self.assertRaises(TypeError):
            r = Rectangle(3)
        with self.assertRaises(TypeError):
            r = Rectangle(3, 6, 0, 0, 9, 7)
    
    def test_with_correct_args(self):
        """ test with correct args"""
        r1 = Rectangle(3, 6, 0, 0, 9)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 6)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, 9)

    def test_wrong_data_type(self):
        """ Wrong data type """
        with self.assertRaises(TypeError):
            r2 = Rectangle(3, "a")
        with self.assertRaises(TypeError):
            r2 = Rectangle("a", 3)
        with self.assertRaises(TypeError):
            r2 = Rectangle(3, 6, "a", 9)
        with self.assertRaises(TypeError):
            r2 = Rectangle(3, 6, 2, "a")

    def test_wrong_int_range(self):
        """ wrong integer range """
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 6)
        with self.assertRaises(ValueError):
            r3 = Rectangle(3, 0)
        with self.assertRaises(ValueError):
            r3 = Rectangle(3, 6, -1)
        with self.assertRaises(ValueError):
            r3 = Rectangle(3, 6, 1, -1)

    '---------- Test area method ----------'

    def test_area(self):
        """ area method unittest """
        r4 = Rectangle(5, 5)
        self.assertEqual(r4.area(), 25)

    def test_area_no_args(self):
        """ test area arguments """
        with self.assertRaises(TypeError):
            Rectangle.area()

    '---------- Test display method ----------'

    def test_display(self):
        """ Test display method """
        output = io.StringIO()
        sys.stdout = output
        r5 = Rectangle(3, 2)
        r5.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "###\n###\n")

    def test_updated_display(self):
        """ display unittest """
        output = io.StringIO()
        sys.stdout = output
        r5 = Rectangle(3, 2, 1, 0)
        r5.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), " ###\n ###\n")
    '---------- Test __str__ method ----------'

    def test_str(self):
        """ __str__ unittest """
        r6 = Rectangle(2, 2, 0, 0, 29)
        p = r6.__str__()
        self.assertEqual(p, "[Rectangle] (29) 0/0 - 2/2")
        r6 = Rectangle(4, 6, 2, 1, 12)
        p = r6.__str__()
        self.assertEqual(p, "[Rectangle] (12) 2/1 - 4/6")

    '---------- Test Update method ----------'

    def test_update_no_agrs(self):
        """ update unittest """
        r7 = Rectangle(3, 6)
        with self.assertRaises(TypeError):
            Rectangle.update()

    def test_update(self):
        """ update method unittest """
        r7 = Rectangle(3, 6)
        r7.update(3)
        self.assertEqual(r7.id, 3)
        r7.update(3, 6, 2)
        self.assertEqual(r7.id, 3)
        r7.update(3, 6, 2, 1)
        self.assertEqual(r7.id, 3)
        r7.update(3, 6, 2, 1, 5)
        self.assertEqual(r7.id, 3)
        p = r7.__str__()
        self.assertEqual(p, '[Rectangle] (3) 1/5 - 6/2')

    def test_update_kwargs_height(self):
        """ update unittest """
        r7 = Rectangle(10, 10, 10, 10)
        r7.update(height=1)
        p = r7.__str__()
        self.assertEqual(p, '[Rectangle] (5) 10/10 - 10/1')

    def test_update_kwargs_widht(self):
        """ update unittest """
        r7 = Rectangle(10, 10, 10, 10)
        r7.update(width=2)
        p = r7.__str__()
        self.assertEqual(p, '[Rectangle] (7) 10/10 - 2/10')

    def test_update_kwargs_id_x_y(self):
        """ update unittest """
        r7 = Rectangle(10, 10, 10, 10)
        r7.update(id=9, x=1, y=5)
        p = r7.__str__()
        self.assertEqual(p, '[Rectangle] (9) 1/5 - 10/10')

    '---------- Test to_dictionary method ----------'

    def test_to_dictionary_method(self):
        """ to_dictionary method unittest """
        r8 = Rectangle(2, 2)
        d = r8.to_dictionary()
        self.assertEqual(d['width'], 2)
        self.assertEqual(d['height'], 2)
        self.assertEqual(d['x'], 0)
        self.assertEqual(d['y'], 0)


if __name__ == "__main__":
    unittest.main()
