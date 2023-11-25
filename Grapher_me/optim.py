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

    [x,+,y]
"""
import math
class Calculator:
    def __init__(self):
        self.x_negative = -10
        self.x_positive = 10
        self.decimals = 2
        self.x_negative_in_loop = self.x_negative * (10 ** self.decimals)
        self.x_positive_in_loop = self.x_positive * (10 ** self.decimals)
    def solve(self,string,function_dic):
        return None

    def solve_for_x(self,equation):
        points_list = []
        for x_in_loop in range(self.x_negative_in_loop,self.x_positive_in_loop+1):
            x = x_in_loop / (10 ** self.decimals)
            equation_to_eval = ""
            for i in equation:
                if i == "x":
                    equation_to_eval += str("("+str(x)+")")
                else:
                    equation_to_eval += i
            answer = eval(equation_to_eval)
            points_list.append([x,answer])
        print(len(points_list))
        return points_list
if __name__ == "__main__":
    cal = Calculator()
    print(cal.solve_for_x('x**(2)'))
