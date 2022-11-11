import unittest


def add(number1,number2):
    """
    Adds two Integers
    """
    return number1+number2
    
def subtract(number1,number2):
    """
    Subtracts two Integers
    """
    return number1-number2

def product(number1,number2):
    """
    Multiplication of two Integers
    """
    return number1*number2


def divide(num1,num2):
    if num2==0:
        raise ValueError("Can't divide by zero")
    return num1/num2

    
class TestCalc(unittest.TestCase):


    def test_add(self):
        self.assertEqual(add(2,10), 12)
        self.assertEqual(add(-4,4), 0)


    def test_substract(self):
        self.assertEqual(subtract(2,-10), 12)
        self.assertEqual(subtract(-4,-4), 0)


    def test_multiply(self):
        self.assertEqual(product(5,-9), -45)
        self.assertEqual(product(4,0), 0)
        self.assertEqual(product(-10,-5), 50)


    def test_divide(self):
        self.assertEqual(divide(10,2), 5)
        self.assertRaises(ValueError, divide, 10, 0)
        



unittest.main()