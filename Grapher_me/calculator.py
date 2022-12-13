class Calculator:
    def __init__(self, equation, units, sub_units):
        self.answer = 0
        self.solved = False
        self.sub_unit = sub_units
        self.equation = equation
        self.units = units

    def solve(self,equ):
        to_return = []
        if "x" in equ and "y" in equ:
            to_return=self.solve_in_x_and_y()
        elif "x" in equ:
            self.solve_in_x_variables(self.units)
            to_return=self.solve_in_x(equ)
        elif "y" in equ:
            self.solve_in_y_variables(self.units)
            to_return=self.solve_in_y(equ)
        return to_return

    def solve_in_x_variables(self,units):
        self._x = -1 * units
        self.x_ = units + 1
    def solve_in_y_variables(self,units):
        self._y = -1 * units
        self.y_ = units + 1
    def power(self,a,b):
        return a**b

    def divide(self,a,b):
        try:
            return a/b
        except:
            return None

    def multiply(self,a,b):
        return a*b

    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
        return a-b

    def solve_in_x(self,orignal_equ):
        sign_list = [self.power,self.divide,self.multiply,self.add,self.subtract]
        y_list = []
        for x in range(self._x,self.x_):
            true_value = x / self.sub_unit
            y_equ = orignal_equ
            new_y_list = []
            for sign in sign_list:
                sign_name = sign.__name__
                for element_index in range(0,len(y_equ)):
                    if y_equ[element_index] == sign_name:
                        self.solved = True
                        if new_y_list.__getitem__(len(new_y_list)-1) == "x":
                            if y_equ[element_index + 1] == "x":
                                answer = sign(true_value,true_value)
                            else:
                                answer = sign(true_value, y_equ[element_index + 1])
                        elif y_equ[element_index+1] == "x":
                            answer = sign(new_y_list.__getitem__(len(new_y_list)-1),true_value)
                        else:
                            answer = sign(new_y_list.__getitem__(len(new_y_list) - 1),
                                               y_equ[element_index+1])
                        new_y_list.pop()
                        new_y_list.append(answer)
                    else:
                        if self.solved:
                            self.solved = False
                        else:
                            new_y_list.append(y_equ[element_index])
                y_equ = new_y_list
                new_y_list = []
            y_list.append([x,y_equ[0]*self.sub_unit])

        return y_list

    def solve_in_y(self,orignal_equ):
        sign_list = [self.power, self.divide, self.multiply, self.add, self.subtract]
        x_list = []
        for y in range(self._y, self.y_):
            true_value = y / self.sub_unit
            x_equ = orignal_equ
            new_x_list = []
            for sign in sign_list:
                sign_name = sign.__name__
                for element_index in range(0, len(x_equ)):
                    if x_equ[element_index] == sign_name:
                        self.solved = True
                        if new_x_list.__getitem__(len(new_x_list) - 1) == "y":
                            if x_equ[element_index + 1] == "y":
                                answer = sign(true_value, true_value)
                            else:
                                answer = sign(true_value, x_equ[element_index + 1])
                        elif x_equ[element_index + 1] == "y":
                            answer = sign(new_x_list.__getitem__(len(new_x_list) - 1), true_value)
                        else:
                            answer = sign(new_x_list.__getitem__(len(new_x_list) - 1),
                                               x_equ[element_index + 1])
                        new_x_list.pop()
                        new_x_list.append(answer)
                    else:
                        if self.solved:
                            self.solved = False
                        else:
                            new_x_list.append(x_equ[element_index])
                x_equ = new_x_list
                new_x_list = []
            x_list.append([x_equ[0] * self.sub_unit,y])

        return x_list

    def solve_in_x_and_y(self):
        self.sign_list = [self.power, self.divide, self.multiply, self.add, self.subtract]

        for x in range(self._x,self.x_):
            pass




if __name__ == "__main__":
    cal = Calculator(["x","power",1], 500, 50)
    print(cal.solve(["x","power",1]))