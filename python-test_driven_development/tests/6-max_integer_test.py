#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit test class"""
    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_one(self):
        self.assertEqual(max_integer([1]), 1)

    def test_max_beginning(self):
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_one_negative(self):
        self.assertEqual(max_integer([-1, 3]), 3)

    def test_only_negative(self):
        self.assertEqual(max_integer([-1, -2]), -1)
