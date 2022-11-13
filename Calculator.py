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

print ("done")
print ("testing webhooks")
