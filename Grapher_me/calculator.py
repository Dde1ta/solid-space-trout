class Calculator:
    def __init__(self, equation, units, sub_units):
        self.Y_EQUATION = equation
        self.y_equ = self.Y_EQUATION
        self.new_y_list = []
        self.y_list = []
        self.answer = 0
        self.solved = False
        self._x = -1 * units * sub_units
        self.x_ = units*sub_units + 1
        self.sub_unit = sub_units

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

    def solve(self):
        self.sign_list = [self.power,self.divide,self.multiply,self.add,self.subtract]
        for x in range(self._x,self.x_):
            true_value = x / self.sub_unit
            self.y_equ = self.Y_EQUATION
            self.new_y_list = []
            for sign in self.sign_list:
                sign_name = sign.__name__
                for element_index in range(0,len(self.y_equ)):
                    if self.y_equ[element_index] == sign_name:
                        self.solved = True
                        if self.new_y_list.__getitem__(len(self.new_y_list)-1) == "x":
                            if self.y_equ[element_index + 1] == "x":
                                self.answer = sign(true_value,true_value)
                            else:
                                self.answer = sign(true_value, self.y_equ[element_index + 1])
                        elif self.y_equ[element_index+1] == "x":
                            self.answer = sign(self.new_y_list.__getitem__(len(self.new_y_list)-1),true_value)
                        else:
                            self.answer = sign(self.new_y_list.__getitem__(len(self.new_y_list) - 1),
                                               self.y_equ[element_index+1])
                        self.new_y_list.pop()
                        self.new_y_list.append(self.answer)
                    else:
                        if self.solved:
                            self.solved = False
                        else:
                            self.new_y_list.append(self.y_equ[element_index])
                self.y_equ = self.new_y_list
                self.new_y_list = []
            self.y_list.append([x,self.y_equ[0]*self.sub_unit])

        return self.y_list