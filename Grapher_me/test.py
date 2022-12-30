import calculator

cal = calculator.Calculator([["x","add",2],"power",2],500,50)
print(cal.solve([["x"],"power",2]))
print("next")
print(cal.solve(["x","power",2]))