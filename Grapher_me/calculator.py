"""
Returns the list of points:->
    the graph x_axis is from -10 to 10 : 20 squares
    there are 500 pixles: each square has 25px (0.04,0.08,0.12,0.16,...,1,2,...,10)
    x_px = (-250,250): So x = x_px / 25
    That is how we calculate the points
"""
class Calculator:
    def __init__(self,string):
        self.equation_string = string
        self._x_px = -250
        self.x_px = 250
        self.pixles = 25
        self.answer_list = []