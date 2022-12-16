import tkinter as tk
from potter import Graph_frame
import pyautogui as pa
from calculator import Calculator as Cal
from inputer import Inputer_frame
import random as r

class Main:
    def __init__(self,master = None):
        self.master = master
        self.master.geometry(str(master.winfo_screenwidth()) + 'x' + str(master.winfo_screenheight()))
        self.master.state('zoomed')

        self.variables_for_graphs()
        self.variables_for_inputer()
        self.place_frames()
    def variables_for_graphs(self):
        self.HEIGHT = 1000
        self.WIDHT = 1000

        self.graph_frame = tk.Frame(self.master, height=self.HEIGHT, width=self.WIDHT)
        self.graph_canvas = tk.Canvas(self.graph_frame, width=self.WIDHT, height=self.HEIGHT, highlightthickness=1,
                                      highlightbackground="white", bg="black")
        self.graph_canvas.create_line(500, 0, 500, 1000, width=2, fill="white")  # Y_axis
        self.graph_canvas.create_line(0, 500, 1000, 500, width=2, fill="white")  # X_axis
        # list of the hex char. for random colour genration
        self.hex_list = [ '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c']
        self.show_string = ''

        self.graph_frame.place(x=0, y=0)
        self.Equation_list = []
        self.y_axis_values()
        self.x_axis_values()
        self.vertical_grid()
        self.horizontal_grid()
        self.place_coords()
        self.graph_canvas.pack()
    def variables_for_inputer(self):
        self.input_frame = tk.Frame(self.master, height=580, width=920, bg="black")
        self.Equation_list = []
        self.show_string = ''
        self.inputer_objects(self.input_frame)
        self.is_negative = False
        self.adding_digites = False
    def inputer_objects(self, frame):
        """
            add the objects in inputer frame
        :param frame: The inputer frame
        :return:
        """
        self.equation_label = tk.Label(frame,bg = "black",fg = "white")
        self.equation_label.place(x=0, y=0, width=920, height=80)
        self.botton1 = tk.Button(frame, text=1, command=lambda: self.number_botton_pressed(self.botton1))
        self.botton1.place(x=0, y=180, width=184, height=100)
        self.botton2 = tk.Button(frame, text=2, command=lambda: self.number_botton_pressed(self.botton2))
        self.botton2.place(x=184, y=180, width=184, height=100)
        self.botton3 = tk.Button(frame, text=3, command=lambda: self.number_botton_pressed(self.botton3))
        self.botton3.place(x=368, y=180, width=184, height=100)
        self.botton4 = tk.Button(frame, text=4, command=lambda: self.number_botton_pressed(self.botton4))
        self.botton4.place(x=0, y=280, width=184, height=100)
        self.botton5 = tk.Button(frame, text=5, command=lambda: self.number_botton_pressed(self.botton5))
        self.botton5.place(x=184, y=280, width=184, height=100)
        self.botton6 = tk.Button(frame, text=6, command=lambda: self.number_botton_pressed(self.botton6))
        self.botton6.place(x=368, y=280, width=184, height=100)
        self.botton7 = tk.Button(frame, text=7, command=lambda: self.number_botton_pressed(self.botton7))
        self.botton7.place(x=0, y=380, width=184, height=100)
        self.botton8 = tk.Button(frame, text=8, command=lambda: self.number_botton_pressed(self.botton8))
        self.botton8.place(x=184, y=380, width=184, height=100)
        self.botton9 = tk.Button(frame, text=9, command=lambda: self.number_botton_pressed(self.botton9))
        self.botton9.place(x=368, y=380, width=184, height=100)
        self.botton0 = tk.Button(frame, text=0, command=lambda: self.number_botton_pressed(self.botton0))
        self.botton0.place(x=0, y=480, width=184, height=100)
        self.botton_y = tk.Button(frame, text="y", command=self.y_botton_pressed)
        self.botton_y.place(x=552, y=80, width=184, height=100)
        self.botton_bracket_open = tk.Button(frame, text="(")
        self.botton_bracket_open.place(x=552, y=180, width=184, height=100)
        self.botton_bracket_close = tk.Button(frame, text=")")
        self.botton_bracket_close.place(x=552, y=280, width=184, height=100)
        self.botton_decimel = tk.Button(frame, text=".")
        self.botton_decimel.place(x=552, y=380, width=184, height=100)
        self.botton_divide = tk.Button(frame, text="/", command=self.divide_botton_pressed)
        self.botton_divide.place(x=736, y=180, width=184, height=100)
        self.botton_multiply = tk.Button(frame, text="*", command=self.multiply_botton_pressed)
        self.botton_multiply.place(x=736, y=280, width=184, height=100)
        self.botton_add = tk.Button(frame, text="+", command=self.add_botton_pressed)
        self.botton_add.place(x=736, y=380, width=184, height=100)
        self.botton_subtract = tk.Button(frame, text="-", command=self.subtract_botton_pressed)
        self.botton_subtract.place(x=736, y=480, width=184, height=100)
        self.botton_power = tk.Button(frame, text="^", command=self.power_botton_pressed)
        self.botton_power.place(x=736, y=80, width=184, height=100)
        self.botton_x = tk.Button(frame, text="x", command=self.x_botton_pressed)
        self.botton_x.place(x=368, y=80, width=184, height=100)
        self.botton_plot = tk.Button(frame, text="Plot", command=self.polt_botton_pressed)
        self.botton_plot.place(x=184, y=480, width=552, height=100)
        self.botton_num_negative = tk.Button(frame, text="(-)", command=self.negative_botton_pressed)
        self.botton_num_negative.place(x=0, y=80, width=184, height=100)
        self.botton_delete = tk.Button(frame, text="Delete",command = self.delete_botton_pressed)
        self.botton_delete.place(x=184, y=80, width=184, height=100)
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
        cal = Cal(equation, 500, 50)
        return cal.solve(equation)
    def plot(self,equation):
        """
        Plots the points in the list on the graph
        :param equation:
        :return:
        """
        self.points_list = self.calculate(equation)
        line_color = self.random_color()
        n= 0
        print(self.points_list)

        if "x" in equation and "y" in equation:
            print("yes")
            for i in range(0, len(self.points_list)):
                try:
                    # correction for the shift in orign from tk's (0,0) to tk's (500,500)
                    self.graph_canvas.create_line(self.points_list[i][0] + 500,
                                                  -1 * self.points_list[i][1] + 500,
                                                  self.points_list[i + 2][0] + 500,
                                                  -1 * self.points_list[i + 2][1] + 500,
                                                  fill=line_color, tags=self.show_string)
                    self.graph_canvas.update()
                    self.graph_frame.update()
                except:
                    self.graph_canvas.create_line(self.points_list[i][0] + 500,
                                                  -1 * self.points_list[i][1] + 500,
                                                  self.points_list[0][0] + 500,
                                                  -1 * self.points_list[0][1] + 500,
                                                  fill=line_color, tags=self.show_string)
                    self.graph_canvas.update()
        else:
            print("no")
            for i in range(0, len(self.points_list)):
                try:
                    # correction for the shift in orign from tk's (0,0) to tk's (500,500)
                    self.graph_canvas.create_line(self.points_list[i][0] + 500,
                                                  -1 * self.points_list[i][1] + 500,
                                                  self.points_list[i + 1][0] + 500,
                                                  -1 * self.points_list[i + 1][1] + 500,
                                                  fill=line_color, tags=self.show_string)
                    self.graph_canvas.update()
                    self.graph_frame.update()
                except:
                    self.graph_canvas.update()
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
    def number_botton_pressed(self, botton):
        print(self.adding_digites,self.Equation_list[-1])
        if self.adding_digites:
            if self.is_negative:
                num = (int(self.Equation_list.pop())*10 + int(botton["text"]))* -1
                self.Equation_list.append(num)
            else:
                num = int(self.Equation_list.pop())*10 + botton["text"]
                self.Equation_list.append(num)
            new_show = ""
            for char_i in range(len(self.show_string)-1):
                new_show+=self.show_string[char_i]
                print(new_show)
            self.show_string = new_show
            self.show_string += str(num)
        else:
            if self.is_negative:
                num = int(botton["text"]) * -1
                self.Equation_list.append(num)
            else:
                num = botton["text"]
                self.Equation_list.append(botton["text"])
            self.adding_digites = True
            self.show_string += str(num)
        self.equation_label.config(text=self.show_string)
    def power_botton_pressed(self):
        self.Equation_list.append("power")
        self.show_string += "^"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def divide_botton_pressed(self):
        self.Equation_list.append("divide")
        self.show_string += "/"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def multiply_botton_pressed(self):
        self.Equation_list.append("multiply")
        self.show_string += "*"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def add_botton_pressed(self):
        self.Equation_list.append("add")
        self.show_string += "+"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def subtract_botton_pressed(self):
        self.Equation_list.append("subtract")
        self.show_string += "-"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def x_botton_pressed(self):
        self.Equation_list.append("x")
        self.show_string += "x"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def y_botton_pressed(self):
        self.Equation_list.append("y")
        self.show_string += "y"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def polt_botton_pressed(self):
        self.show_on_top = self.show_string
        print(self.show_on_top,self.Equation_list)


        self.plot(self.Equation_list)

        self.Equation_list = []
        self.equation_label.config(text = "")
        self.show_string = ""
        self.adding_digites = False
    def delete_botton_pressed(self):
        show_string_new = ''
        for i in range(len(self.show_string)-1):
            show_string_new += self.show_string[i]
        self.show_string = show_string_new
        self.equation_label.config(text = self.show_string)
        if type(self.Equation_list[-1]) == type(1):
            if self.Equation_list[-1]/10 > 10 :
                pass
            else:
                self.adding_digites = False
        try:
            self.Equation_list.pop()
        except:
            pass
    def negative_botton_pressed(self):
        if self.is_negative:
            self.is_negative = False
        else:
            self.is_negative = True
        self.adding_digites = False
    def place_frames(self):
        self.graph_frame.place(x=0,y=0)
        self.input_frame.place(x=1000, y=450)

if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="black")
    main = Main(root)
    root.mainloop()