import tkinter as tk
from calculator import Calculator as Cal
import pyautogui as pa
import random as r

class Graph_frame:
    def __init__(self,master = None):
        self.master = master
        self.HEIGHT = 1000
        self.WIDHT = 1000


        self.graph_frame = tk.Frame(self.master,height=self.HEIGHT,width = self.WIDHT)
        self.graph_canvas = tk.Canvas(self.graph_frame, width=self.WIDHT, height=self.HEIGHT, highlightthickness=1,
                                      highlightbackground="white", bg = "black")
        self.graph_canvas.create_line(500, 0, 500, 1000, width=2, fill ="white") #Y_axis
        self.graph_canvas.create_line(0, 500, 1000, 500, width=2, fill ="white") #X_axis
        # list of the hex char. for random colour genration
        self.hex_list = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']
        self.show_string = ''
        
        self.graph_frame.place(x= 0,y =0 )
        self.input_frame = tk.Frame(master, height=580, width=920, bg="black")
        self.objects(self.input_frame)
        self.Equation_list = []
        self.y_axis_values()
        self.x_axis_values()
        self.vertical_grid()
        self.horizontal_grid()
        self.place_coords()
        self.graph_canvas.pack()

    def vertical_grid(self):
        """
        For the creation of grid lines
            -> seprated by 50 px
            -> 1 px = 0.02 units in the y-axis
        :return:
        """

        for i in range(0,1000,50):
            if i == 500:
                pass
            else:
                self.graph_canvas.create_line(i, 0, i, 1000, width=0.01, fill="gray")

    def horizontal_grid(self):
        """
        For the creation of horizontal lines
            -> seprated by 50 px
            -> 1 px = 0.02 units in the x-axis
        :return:
        """
        for i in range(0,1000,50):
            if i == 500:
                pass
            else:
                self.graph_canvas.create_line(0, i, 1000, i, fill="gray")

    def y_axis_values(self):
        """
        Creates the y-axis numbers
        :return:
        """
        # the +ve y axis values
        self.y_axis_values_list_positive = [tk.Label(self.graph_frame,text = i,bg = "black",fg = "white") for i in range(10,-1,-1)]
        # the -ve y axis values
        self.y_axis_values_list_negative = [tk.Label(self.graph_frame,text = i,bg = "black",fg = "white") for i in range(-1,-11,-1)]

        # places each label in reveres
        for n in range(11):
            self.y_axis_values_list_positive[n].place(x = 510,y = n*50-10)

        for n in range(10):
            self.y_axis_values_list_negative[n].place(x=510, y=((n+11) * 50)-14)

    def x_axis_values(self):
        """
        Creates the x-axis numbers
        :return:
        """
        self.x_axis_values_list_positive = [tk.Label(self.graph_frame, text=i, bg="black", fg="white") for i in
                                            range(1,10)]
        self.x_axis_values_list_negative = [tk.Label(self.graph_frame, text=i, bg="black", fg="white") for i in
                                            range(-10,0)]
        for n in range(10):
            self.x_axis_values_list_negative[n].place(x = 50*n -8,y = 510)
        for n in range(9):
            self.x_axis_values_list_positive[n].place(x = (50 * (n+10)) +40, y = 510)

    def calculate(self,equation):
        """
        calls the calculator module
        :param equation:
        :return: the list of points
        """
        cal = Cal(equation, 400, 50)
        return cal.solve()

    def plot(self,equation):
        """
        Plots the points in the list on the graph
        :param equation:
        :return:
        """
        points_list = self.calculate(equation)
        line_color = self.random_color()
        print(points_list)
        n= 0

        for i in range(0, len(points_list)):
            try:
                # correction for the shift in orign from tk's (0,0) to tk's (500,500)
                self.graph_canvas.create_line(points_list[i][0] + 500,
                                              -1 *  points_list[i][1] + 500,
                                              points_list[i+1][0] + 500,
                                              -1 * points_list[i+1][1] + 500, fill = "white")
                self.graph_canvas.update()
            except:
                self.graph_canvas.update()

        print("ploted")

    def on_canvas(self,cords):
        """
        Checks for the location of the mouse
        :param cords:
        :return: Boolean
        """
        if cords[0] <1000 and cords[1] <1000:
            return True
        else:
            return False

    def place_coords(self):
        """
        Places the relavtive coords for the mouse

        :return:
        """
        self.mouse = pa.position()
        self.mouse_coords = [self.mouse.x, self.mouse.y]
        if self.on_canvas(self.mouse_coords):
            self.graph_canvas.delete("coords")
            #using pyautogui it returns the position of the moues relavtive to the screen
            #correst the position to be relavtive to the orign of the graph and in right units
            self.graph_canvas.create_text(self.mouse_coords[0] + 20, self.mouse_coords[1] - 50,
                                          text=str((self.mouse_coords[0] - 500)/50)+","+str(-1*((self.mouse_coords[1]-30) - 500)/50),
                                          fill = 'white',
                                          tag = "coords")
        else:
            pass
        self.graph_frame.after(1, self.place_coords)#updates position after 1 ms

    def random_color(self):
        """
        Genrates random hexcode of a color
        :return: hexcode
        """
        colour_code = "#"
        for i in range(6):
            colour_code += r.choice(self.hex_list)
        return colour_code
