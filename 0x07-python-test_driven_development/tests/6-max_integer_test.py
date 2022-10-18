#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_complete_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)

    def test_max_empty_list(self):
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer, None)

    def test_max_str_val_list(self):
        self.assertRaises(TypeError, max_integer, ["a", 2, 3, 4])

    def test_max_None_list(self):
        self.assertRaises(TypeError, max_integer, [1, 2, None, 4])
