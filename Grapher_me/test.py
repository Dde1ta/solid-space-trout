import calculator

cal = calculator.Calculator([2, 'multiply', 'x', 'divide', ['x', 'subtract', 3]],500,50)
print(cal.solve([2, 'multiply', 'x', 'divide', ['x', 'subtract', 3]]))
