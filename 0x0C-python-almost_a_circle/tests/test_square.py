#!/usr/bin/python3
"""
    Rectangle class unittest
"""
import unittest
import sys
import io
from models.rectangle import Rectangle
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """ class TestSquare """

    def test_inheritance(self):
        """ test inheritance """
        self.assertTrue(issubclass(Square, Base))

    def test_square__args(self):
        """ test arguments """
        with self.assertRaises(TypeError):
            s = Square()
        with self.assertRaises(TypeError):
            s = Square(3, 6, 0, 0, 9, 7)
    
    def test_with_correct_args(self):
        """ test with correct args"""
        s1 = Square(3, x=1, y=2, id=9)
        self.assertEqual(s1.id, 9)
        self.assertEqual(s1.__str__(), '[Square] (9) 1/2 - 3')
        self.assertEqual(s1.area(), 9)

    def test_wrong_data_type(self):
        """ Wrong data type """
        with self.assertRaises(TypeError):
            s2 = Square("a")

    def test_wrong_int_range(self):
        """ wrong integer range """
        with self.assertRaises(ValueError):
            s3 = Square(-6)

    '---------- Test area method ----------'

    def test_area(self):
        """ area method unittest """
        s4 = Square(5)
        self.assertEqual(s4.area(), 25)

    def test_area_no_args(self):
        """ test area arguments """
        with self.assertRaises(TypeError):
            Square.area()

    '---------- Test display method ----------'

    def test_display(self):
        """ Test display method """
        output = io.StringIO()
        sys.stdout = output
        s5 = Square(2)
        s5.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "##\n##\n")

    def test_updated_display(self):
        """ display unittest """
        output = io.StringIO()
        sys.stdout = output
        s5 = Square(2, x=1, y=1)
        s5.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n ##\n ##\n")

    '---------- Test __str__ method ----------'

    def test_str(self):
        """ __str__ unittest """
        s6 = Square(2, id=29)
        p = s6.__str__()
        self.assertEqual(p, "[Square] (29) 0/0 - 2")

    '---------- Test Update method ----------'

    def test_update_agrs(self):
        """ update unittest """
        s7 = Square(1)
        Square.update(1)
        self.assertEqual(s7.__str__(), "[Square] (22) 0/0 - 1")
        Square.update(1, 3)
        self.assertEqual(s7.__str__(), "[Square] (1) 0/0 - 3")
        Square.update(1, 3, 2, 4)
        self.assertEqual(s7.__str__(), "[Square] (1) 2/4 - 3")

    def test_update_kwargs(self):
        """ update unittest """
        s7 = Square(id=3, x=2, y=5, size=7)
        Square.update(1)
        self.assertEqual(s7.__str__(), "[Square] (23) 2/5 - 7")

    '---------- Test to_dictionary method ----------'

    def test_to_dictionary_method(self):
        """ to_dictionary method unittest """
        s8 = Square(2)
        d = s8.to_dictionary()
        self.assertEqual(d, dict)
        self.assertEqual(d['id'], 29)
        self.assertEqual(d['size'], 2)
        self.assertEqual(d['x'], 0)
        self.assertEqual(d['y'], 0)


if __name__ == "__main__":
    unittest.main()
