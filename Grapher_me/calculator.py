"""
Returns the list of points:->
    the graph x_axis is from -10 to 10 : 20 squares
    there are 500 pixles: each square has 25px (0.04,0.08,0.12,0.16,...,1,2,...,10)
    x_px = (-250,250): So x = x_px / 25
    That is how we calculate the points
"""
class Calculator:
    def __init__(self):
        self._x_px = -250
        self.x_px = 250
        self.pixles = 25

    def solve_final_x(self,string):
        points_list = []
        for x in range(self._x_px,self.x_px+1):
            string_to_eval = ""
            for s in string:
                if s == "x":
                    string_to_eval += str(x/25)
                else:
                    string_to_eval += s
            answer = eval(string_to_eval)
            points_list.append([x/25,answer])
        return points_list

    def solve_final_y(self,string):
        points_list = []
        for y in range(self._x_px,self.x_px+1):
            string_to_eval = ""
            for s in string:
                if s == "y":
                    string_to_eval += str(y/25)
                else:
                    string_to_eval += s
            answer = eval(string_to_eval)
            points_list.append([answer,y/25])
        return points_list

    def solve_final_x_y(self,string):
        points_list = []
        for x in range(self._x_px,self.x_px+1):
            for y in range(self._x_px, self.x_px + 1):
                string_to_eval = ""
                for s in string:
                    if s == "y":
                        string_to_eval += str(y / 25)
                    elif s == "x":
                        string_to_eval += str(x / 25)
                    else:
                        string_to_eval += s
                answer = eval(string_to_eval)
                print(x/25,y/25,answer,string_to_eval)
                input()
                if answer == 0:
                    points_list.append([x / 25, y / 25])
        return points_list

if __name__ == "__main__":
    cal = Calculator()
    points = cal.solve_final_x("(x**2)")
    print(points)