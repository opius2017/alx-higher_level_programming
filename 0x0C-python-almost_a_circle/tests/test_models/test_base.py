#!/usr/bin/python3
"""
This module contains unit tests for the Base class.
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def test_init(self):
        """Test the __init__ method of Base class."""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base(0)
        self.assertEqual(b4.id, 0)

        b5 = Base(-3)
        self.assertEqual(b5.id, -3)


if __name__ == '__main__':
    unittest.main()
