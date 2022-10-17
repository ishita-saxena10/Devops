import unittest
from Calculator import add, subtract,product, divide

class TestCalc(unittest.TestCase):


    def test_add(self):
        self.assertEqual(add(5,10), 15)
        self.assertEqual(add(-2,2), 0)
        self.assertEqual(add(-1,-5), -6)


    def test_substract(self):
        self.assertEqual(subtract(5,-10), 15)
        self.assertEqual(subtract(-2,-2), 0)
        self.assertEqual(subtract(1,5), -4)


    def test_multiply(self):
        self.assertEqual(product(5,-9.0), -45)
        self.assertEqual(product(-2,0), 0)
        self.assertEqual(product(-10,-5), 50)


    def test_divide(self):
        self.assertEqual(divide(5,2), 2.5)
        self.assertRaises(ValueError, divide, 10, 0)
        



unittest.main()