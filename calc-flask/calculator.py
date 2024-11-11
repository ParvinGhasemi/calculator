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
