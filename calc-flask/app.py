from flask import Flask, render_template, request, abort
from calculator import Calculator

calc = Calculator()
app = Flask(__name__)


@app.route('/')
def render_index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form.get('num1'))
        num2 = float(request.form.get('num2')) if request.form.get('num2') else None
        operation = request.form.get('operation')
    except ValueError:
        #   return('Invalid input! Please input a valid number: integers or decimals.')
        abort(400, desciption='Invalid input! Please input a valid number: integers or decimals.')
        #   raise ValueError('Invalid input! Please input a valid number: integers or decimals.')


    match operation:
        case 'add':
            result = calc.add(num1, num2)
        case 'subtract':
            result = calc.subtract(num1, num2)
        case 'multiply':
            result = calc.multiply(num1, num2)
        case 'divide':
            result = calc.divide(num1, num2)
        case 'power':
            result = calc.power(num1, num2)
        case 'modulo':
            result = calc.modulo(num1, num2)
        case 'sqrt':
            result = calc.sqrt(num1)
        case _:
            return 'Invalid Opertation'
        
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
