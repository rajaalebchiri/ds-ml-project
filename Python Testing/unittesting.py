# unittesting.py
import unittest

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        if self.width <= 0 or self.height <= 0:
            return -1
        return self.width * self.height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

def add_amount(n):
    if n < 0:
        raise ValueError("amount must be positive")
    return "available amount {}".format(n)

class TestGetAreaRectangle(unittest.TestCase):
    def test_normal_case(self):
        rectange = Rectangle(2,3)
        self.assertEqual(rectange.get_area(), 6, "incorrect area")
    def test_negative_case(self):
        """expect -1 as output to denote error when looking at negative area"""
        rectange = Rectangle(-1,2)
        self.assertEqual(rectange.get_area(), -1, "incorrect negative output")

class TestAddAmount(unittest.TestCase):
    def test_add_amount(self):
        actual = add_amount(30)
        expected = "available amount 30"
        self.assertEqual(actual, expected)
    def test_add_amount_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            add_amount(-1)
        self.assertEqual(str(exception_context.exception), "amount must be positive")

if __name__ == "__main__":
    unittest.main()