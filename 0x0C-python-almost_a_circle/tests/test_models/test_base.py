#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_missing_id(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_supplied_id(self):
        base1 = Base(50)
        self.assertEqual(base1.id, 50)

    def test_new_id(self):
        base1 = Base()
        base2 = Base(50)
        base3 = Base()
        self.assertEqual(base1.id, base3.id - 1)

    def test_neg_id(self):
        base1 = Base(-2)
        self.assertEqual(base1.id, -2)

    def test_str(self):
        base1 = Base("Hi")
        self.assertEqual(base1.id, "Hi")

    def test_float_id(self):
        self.assertEqual(Base(3.2).id, 3.2)

    def test_errors(self):
        with self.assertRaises(TypeError):
            base1 = Base(1, 2)


if __name__ == "__main__":
    unittest.main()
