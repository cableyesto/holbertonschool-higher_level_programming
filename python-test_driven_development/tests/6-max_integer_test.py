#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit test class"""
    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_normal(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
