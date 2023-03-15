"""
Returns the list of points:->
    the graph x_axis is from -10 to 10 : 20 squares
    there are 1000 pixles: each square has 50px (0.04,0.08,0.12,0.16,...,1,2,...,10)
    x_px = (-250,250): So x = x_px / 25
    That is how we calculate the points

    to do planfor functions
    "[x]+{x}"([.] G.I.F and {.} F.P.F)
    funct_dict = {GIF:"0",FPF:"4"}
    if not then {}
"""
import math
class Calculator:
    def __init__(self):
        self._x_px = -500
        self.x_px = 500
        self.pixles = 25
        self.change_in_index = 0

    def solve(self,string,function_dic):
        if "x" in string and "y" in string:
            to_return = self.solve_final_x_y(string)
        elif "y" in string:
            to_return = self.solve_final_y(string)
        else:
            to_return = self.solve_final_x(string,function_dic)

        return to_return
    def gif(self,string,index,n):
        og_string = string
        new_string = ""
        string_to_eval = ""
        operation_string = ""
        open_ = False
        for i in string:
            if open_ and i != "]":
                operation_string += i
            if i == "[":
                open_ = True
            elif i == "]":
                open_ = False
                break


        for s in operation_string:
            if s == "x" or s == "y":
                string_to_eval += "("
                string_to_eval += str(n / 50)
                string_to_eval += ")"

            else:
                string_to_eval += s


        answer = math.floor(eval(string_to_eval+"+ 0"))
        self.change_in_index += len(operation_string) - len(str(answer))

        for i in range(len(og_string)):


            if og_string[i] == "[":
                open_ = True
            if i == index:
                new_string += "("
                new_string += str(answer)
                new_string += ")"
            else:
                if open_:
                    pass
                else:
                    new_string += str(og_string[i])
                if og_string[i] == "[":
                    open_ = True
                if og_string[i] == "]":
                    open_ = False

        return new_string
    def mod(self,string,index,n):
        og_string = string
        new_string = ""
        string_to_eval = ""
        operation_string = ""
        open_ = False
        for i in string:
            if open_ and i != ">":
                operation_string += i
            if i == "<":
                open_ = True
            elif i == ">":
                open_ = False
                break

        for s in operation_string:
            if s == "x" or s == "y":
                string_to_eval += "("
                string_to_eval += str(n / 50)
                string_to_eval += ")"

            else:
                string_to_eval += s

        if eval(string_to_eval) >0 :
            answer = eval(string_to_eval)
        else:
            answer = eval(string_to_eval)*-1

        for i in range(len(og_string)):

            if og_string[i] == "<":
                open_ = True
            if i == index:
                new_string += "("
                new_string += str(answer)
                new_string += ")"

            else:
                if open_:
                    pass
                else:
                    new_string += str(og_string[i])
                if og_string[i] == "<":
                    open_ = True
                if og_string[i] == ">":
                    open_ = False

        self.change_in_index += len(operation_string) - len(str(answer))

        return new_string
    def solve_final_x(self,string,function_dic):
        print("here")
        points_list = []
        for x in range(self._x_px,self.x_px+1):
            self.change_in_index = 0
            string_to_eval = ""
            string_ = string
            n_of_change = 0
            for function_ in function_dic:
                if function_ == "GIF":
                    string_ = self.gif(string_,function_dic[function_]-self.change_in_index+1,x)
                elif function_ == "MOD":
                    string_ = self.mod(string_,function_dic[function_]-self.change_in_index+1,x)

            try:
                for s in string_:
                    if s == "x":
                        string_to_eval += "("
                        string_to_eval += str(x / 50)
                        string_to_eval += ")"

                    else:
                        string_to_eval += s
                answer = eval(string_to_eval)



                points_list.append([x / 50, answer])
                #print(string_to_eval,"+",answer)
                #input()
            except:
                pass
        return points_list
    def solve_final_y(self,string):
        points_list = []
        for y in range(self._x_px,self.x_px+1):
            string_to_eval = ""
            try:
                for s in string:
                    if s == "y":
                        string_to_eval += "("
                        string_to_eval += str(y / 50)
                        string_to_eval += ")"
                    else:
                        string_to_eval += s
                answer = eval(string_to_eval)
                points_list.append([answer, y / 50])
            except:
                pass
        return points_list
    def solve_final_x_y(self,string):
        points_list = []
        for x in range(self._x_px,self.x_px+1):
            print(x)
            for y in range(self._x_px,0):
                string_to_eval = ""
                try:
                    for s in string:
                        if s == "y":
                            string_to_eval += "("
                            string_to_eval += str(y / 50)
                            string_to_eval += ")"
                        elif s == "x":
                            string_to_eval += "("
                            string_to_eval += str(x / 50)
                            string_to_eval += ")"
                        else:
                            string_to_eval += s
                    answer = eval(string_to_eval)
                    if answer == 0:
                        points_list.append([x / 50, y / 50])
                except:
                    pass
        for x in range(self._x_px, self.x_px + 1):
            print(x)
            for y in range(0, self.x_px + 1):
                string_to_eval = ""
                try:
                    for s in string:
                        if s == "y":
                            string_to_eval += "("
                            string_to_eval += str(y / 50)
                            string_to_eval += ")"
                        elif s == "x":
                            string_to_eval += "("
                            string_to_eval += str(x / 50)
                            string_to_eval += ")"
                        else:
                            string_to_eval += s
                    answer = eval(string_to_eval)
                    if answer == 0:
                        points_list.append([x / 50, y / 50])
                except:
                    pass
        print(points_list)
        return points_list

if __name__ == "__main__":
    cal = Calculator()
    print(cal.solve('x**(1/3)', {}))
