class Calculator:

    def __init__(self, equation, units, sub_units):
        self.answer = 0
        self.solved = False
        self.sub_unit = sub_units
        self.equation = equation
        self.units = units

    def solve(self,equ):
        to_return = []
        if self.has_brackets(equ):
            for i in equ:
                try:
                    if "x" in i and "y" in i:
                        self.solve_in_x_variables(self.units)
                        self.solve_in_y_variables(self.units)
                        to_return = self.solve_in_x_and_y(equ)
                        break
                    elif "x" in i:
                        self.solve_in_x_variables(self.units)
                        to_return = self.solve_in_x(equ)
                        break
                    elif "y" in i:
                        self.solve_in_y_variables(self.units)
                        to_return = self.solve_in_y(equ)
                        break
                except:
                    pass
        elif "x" in equ and "y" in equ:
            self.solve_in_x_variables(self.units)
            self.solve_in_y_variables(self.units)
            to_return=self.solve_in_x_and_y(equ)
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

    def has_brackets(self,equ):
        has_bracket = False

        for i in equ:
            if type([]) == type(i):
                has_bracket = True
                break
            else:
                pass
        return has_bracket

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
            y_equ = []
            for i in orignal_equ:
                if type(i) == type([]):
                    y_equ.append(self.solve_in_a_single_x(true_value,i))
                else:
                    y_equ.append(i)
            new_y_list = []
            for sign in sign_list:
                sign_name = sign.__name__
                for element_index in range(0,len(y_equ)):
                    try:
                        if y_equ[element_index] == sign_name:
                            self.solved = True
                            if new_y_list.__getitem__(len(new_y_list) - 1) == "x":
                                if y_equ[element_index + 1] == "x":
                                    answer = sign(true_value, true_value)
                                else:
                                    answer = sign(true_value, y_equ[element_index + 1])
                            elif y_equ[element_index + 1] == "x":
                                answer = sign(new_y_list.__getitem__(len(new_y_list) - 1), true_value)
                            else:
                                answer = sign(new_y_list.__getitem__(len(new_y_list) - 1),
                                              y_equ[element_index + 1])
                            new_y_list.pop()
                            new_y_list.append(answer)
                        else:
                            if self.solved:
                                self.solved = False
                            else:
                                new_y_list.append(y_equ[element_index])
                    except:
                        pass
                y_equ = new_y_list
                new_y_list = []
            try:
                y_list.append([x,y_equ[0]*self.sub_unit])
            except:
                pass
        return y_list

    def solve_in_a_single_x(self, value, equ):
        y_equ = equ
        sign_list = [self.power,self.divide,self.multiply,self.add,self.subtract]
        true_value = value
        new_y_list = []
        for sign in sign_list:
            sign_name = sign.__name__
            for element_index in range(0, len(y_equ)):
                try:
                    if y_equ[element_index] == sign_name:
                        self.solved = True
                        if new_y_list.__getitem__(len(new_y_list) - 1) == "x":
                            if y_equ[element_index + 1] == "x":
                                answer = sign(true_value, true_value)
                            else:
                                answer = sign(true_value, y_equ[element_index + 1])
                        elif y_equ[element_index + 1] == "x":
                            answer = sign(new_y_list.__getitem__(len(new_y_list) - 1), true_value)
                        else:
                            answer = sign(new_y_list.__getitem__(len(new_y_list) - 1),
                                          y_equ[element_index + 1])
                        new_y_list.pop()
                        new_y_list.append(answer)
                    else:
                        if self.solved:
                            self.solved = False
                        else:
                            new_y_list.append(y_equ[element_index])
                except:
                    pass
            y_equ = new_y_list

            new_y_list = []
        return y_equ[0]

    def solve_in_y(self,orignal_equ):
        sign_list = [self.power, self.divide, self.multiply, self.add, self.subtract]
        x_list = []

        for y in range(self._y, self.y_):
            true_value = y / self.sub_unit
            x_equ = []
            for i in orignal_equ:
                if type(i) == type([]):
                     x_equ.append(self.solve_in_a_single_y(true_value,i))
                else:
                    x_equ.append(i)
            new_x_list = []
            for sign in sign_list:
                sign_name = sign.__name__
                for element_index in range(0, len(x_equ)):
                    try:
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
                    except:
                        pass
                x_equ = new_x_list
                new_x_list = []
            try:
                x_list.append([x_equ[0] * self.sub_unit, y])
            except:
                pass
        return x_list

    def solve_in_a_single_y(self,value,equ):
        x_equ = equ
        sign_list = [self.power,self.divide,self.multiply,self.add,self.subtract]
        true_value = value
        new_x_list = []
        for sign in sign_list:
            sign_name = sign.__name__
            for element_index in range(0, len(x_equ)):
                try:
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
                except:
                    pass
            x_equ = new_x_list
            new_x_list = []
        return x_equ[0]

    def solve_in_x_and_y(self,orignal_equ):
        sign_list = [self.power, self.divide, self.multiply, self.add, self.subtract]
        x_y_equation = orignal_equ
        points_list = []
        new_x_y_list = []
        answer = 0
        for x in range(self._x,self.x_):
            true_value_x = x / self.sub_unit
            new_x_y_list = []
            x_y_equation = orignal_equ
            for y in range(self._y,0):
                true_value_y = y / self.sub_unit
                x_y_equation = orignal_equ
                new_x_y_list = []
                for sign in sign_list:
                    sign_name = sign.__name__
                    for element_index in range(0, len(x_y_equation)):
                        try:
                            if x_y_equation[element_index] == sign_name:
                                self.solved = True
                                if new_x_y_list.__getitem__(len(new_x_y_list) - 1) == "y":
                                    if x_y_equation[element_index + 1] == "y":
                                        answer = sign(true_value_y, true_value_y)
                                    elif x_y_equation[element_index + 1] == "x":
                                        answer = sign(true_value_y, true_value_x)
                                    else:
                                        answer = sign(true_value_y, x_y_equation[element_index + 1])
                                elif new_x_y_list.__getitem__(len(new_x_y_list) - 1) == "x":
                                    if x_y_equation[element_index + 1] == "y":
                                        answer = sign(true_value_x, true_value_y)
                                    elif x_y_equation[element_index + 1] == "x":
                                        answer = sign(true_value_x, true_value_x)
                                    else:
                                        answer = sign(true_value_x, x_y_equation[element_index + 1])
                                elif x_y_equation[element_index + 1] == "y":
                                    answer = sign(new_x_y_list.__getitem__(len(new_x_y_list) - 1), true_value_y)
                                elif x_y_equation[element_index + 1] == "x":
                                    answer = sign(new_x_y_list.__getitem__(len(new_x_y_list) - 1), true_value_x)
                                else:
                                    answer = sign(new_x_y_list.__getitem__(len(new_x_y_list) - 1),
                                                  x_y_equation[element_index + 1])
                                new_x_y_list.pop()
                                new_x_y_list.append(answer)
                            else:
                                if self.solved:
                                    self.solved = False
                                else:
                                    new_x_y_list.append(x_y_equation[element_index])
                        except:
                            pass
                    x_y_equation = new_x_y_list
                    new_x_y_list = []
                if x_y_equation [0] == 0:
                    points_list.append([x,y])
                    break

        for x in range(self._x,self.x_):
            true_value_x = x / self.sub_unit
            new_x_y_list = []
            x_y_equation = orignal_equ
            for y in range(0,self.y_):
                true_value_y = y / self.sub_unit
                x_y_equation = orignal_equ
                new_x_y_list = []
                for sign in sign_list:
                    sign_name = sign.__name__
                    for element_index in range(0, len(x_y_equation)):
                        try:
                            if x_y_equation[element_index] == sign_name:
                                self.solved = True
                                if new_x_y_list.__getitem__(len(new_x_y_list) - 1) == "y":
                                    if x_y_equation[element_index + 1] == "y":
                                        answer = sign(true_value_y, true_value_y)
                                    elif x_y_equation[element_index + 1] == "x":
                                        answer = sign(true_value_y, true_value_x)
                                    else:
                                        answer = sign(true_value_y, x_y_equation[element_index + 1])
                                elif new_x_y_list.__getitem__(len(new_x_y_list) - 1) == "x":
                                    if x_y_equation[element_index + 1] == "y":
                                        answer = sign(true_value_x, true_value_y)
                                    elif x_y_equation[element_index + 1] == "x":
                                        answer = sign(true_value_x, true_value_x)
                                    else:
                                        answer = sign(true_value_x, x_y_equation[element_index + 1])
                                elif x_y_equation[element_index + 1] == "y":
                                    answer = sign(new_x_y_list.__getitem__(len(new_x_y_list) - 1), true_value_y)
                                elif x_y_equation[element_index + 1] == "x":
                                    answer = sign(new_x_y_list.__getitem__(len(new_x_y_list) - 1), true_value_x)
                                else:
                                    answer = sign(new_x_y_list.__getitem__(len(new_x_y_list) - 1),
                                                  x_y_equation[element_index + 1])
                                new_x_y_list.pop()
                                new_x_y_list.append(answer)
                            else:
                                if self.solved:
                                    self.solved = False
                                else:
                                    new_x_y_list.append(x_y_equation[element_index])
                        except:
                            pass
                    x_y_equation = new_x_y_list
                    new_x_y_list = []
                if x_y_equation [0] == 0:
                    points_list.append([x,y])
                    break

        return points_list