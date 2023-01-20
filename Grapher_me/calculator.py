"""
Returns the list of points:->
    the graph x_axis is from -10 to 10 : 20 squares
    there are 1000 pixles: each square has 50px (0.04,0.08,0.12,0.16,...,1,2,...,10)
    x_px = (-250,250): So x = x_px / 25
    That is how we calculate the points
"""
class Calculator:
    def __init__(self):
        self._x_px = -500
        self.x_px = 500
        self.pixles = 25

    def solve(self,string):
        if "x" in string and "y" in string:
            to_return = self.solve_final_x_y(string)
        elif "x" in string:
            to_return = self.solve_final_x(string)
        elif "y" in string:
            to_return = self.solve_final_y(string)

        return to_return

    def solve_final_x(self,string):
        points_list = []
        for x in range(self._x_px,self.x_px+1):
            string_to_eval = ""
            for s in string:
                if s == "x":
                    string_to_eval += "("
                    string_to_eval += str(x/50)
                    string_to_eval += ")"

                else:
                    string_to_eval += s
            answer = eval(string_to_eval)
            points_list.append([x/50,answer])
        return points_list

    def solve_final_y(self,string):
        points_list = []
        for y in range(self._x_px,self.x_px+1):
            string_to_eval = ""
            for s in string:
                if s == "y":
                    string_to_eval += "("
                    string_to_eval += str(y/50)
                    string_to_eval += ")"
                else:
                    string_to_eval += s
            answer = eval(string_to_eval)
            points_list.append([answer,y/50])
        return points_list

    def solve_final_x_y(self,string):
        points_list = []
        for x in range(self._x_px,self.x_px+1):
            for y in range(self._x_px, self.x_px + 1):
                string_to_eval = ""
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
        return points_list

# if __name__ == "__main__":
#     cal = Calculator()
#     points = cal.solve_final_x("(x**2)")
#     print(points)