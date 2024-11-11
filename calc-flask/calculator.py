from math import sqrt

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num1: float, num2: float)-> float:
        self.result = num1 + num2
        return self.result
    

    def subtract(self, num1: float, num2: float)-> float:
        self.result = num1 - num2
        return self.result
    

    def multiply(self, num1: float, num2: float)-> float:
        self.result = num1 * num2
        return self.result
    

    def divide(self, num1: float, num2: float)-> float:
        if num2 == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        self.result = num1 / num2
        return self.result
    
    
    def power(self, num1: float, num2: float)-> float:
        self.result = num1 ** num2
        return self.result
    

    def modulo(self, num1: float, num2: float)-> float:
        self.result = num1 % num2
        return self.result
    
    
    def sqrt(self, num1: float)-> float:
        """Calculate the square root of a non-negative number.
        Parameters:
            num1 (float): A non-negative number to calculate the square root of.
        Returns:
            float: The square root of num1.
        Raises:
            ValueError: If num1 is negative.
        """
        if num1 < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        self.result = sqrt(num1)
        return self.result