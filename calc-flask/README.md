## Calculator - Flask Application
In the flask application, to run the file, you need to have Flask installed. You can install the dependencies by running the requirements file:<br>
`pip install -r requirements.txt`

or you can simply install flask with the command `pip install flask` in your terminal.
> **Note**: It’s recommended to install Flask in a virtual environment to avoid conflicts with other packages.

### Running the Application
To run the application:
1. Go to the directory of your app.py file
2. Run the app by using  `python app.py` or if you're using python 3:<br> `python3 app.py`<br> or simply clicking on the "*Run*" button of your IDE.

Open the local host (http://127.0.0.1:5000) in a web browser; enter values, select operations, and click the *`Calculate`* button to see the result.

---------

### Explain The Approach - Why Not Using Abstraction?
In the beginning, I considered using abstraction and create a subclass for each operation. To make it more clear, here's an example:
```
from abc import ABC, abstractmethod

class CalcOperation(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Add(CalcOperation):
    def execute(self, a, b):
        return a + b

class Subtract(CalcOperation):
    def execute(self, a, b):
        return a - b

class Multiply(CalcOperation):
    def execute(self, a, b):
        return a * b

class Divide(CalcOperation):
    def execute(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b
```

#### Why abstraction?
Using abstraction, follows the **Single Responsibility Principle**, in which each class has one job. It would also make it more **extensible**. Adding a new operation becomes so easy: just create a new class without modifying the existing code. which is following the the **Open/Closed Priciple**.<br><br>


#### Why Using a Single Core Class Instead?
After writing some code and considering this mini project, I decided to use a single class approach. This approach keeps a better balance between readability and functionality for this project; and I like to keep it easier and cleaner.


why? because I wasn't going to make an advanced/scientific calculator. it can be a good approach to add custom behavior and advanced calculations, but I wanted a simple, compact calculator.


-------
I hope this explanation gives you insights into the approach and the reasoning behind the design choices.