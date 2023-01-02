import tkinter as tk
from potter import Graph_frame
import pyautogui as pa
from calculator import Calculator as Cal
from inputer import Inputer_frame
import random as r

class Main:
    def __init__(self,master = None):
        self.master = master
        self.SCREEN_HEIGHT = master.winfo_screenheight()
        self.SCREEN_WIDHT = master.winfo_screenwidth()
        print(self.SCREEN_HEIGHT,self.SCREEN_WIDHT)
        self.master.geometry(str(master.winfo_screenwidth()) + 'x' + str(master.winfo_screenheight()))
        self.master.state('zoomed')
        dpi = master.winfo_fpixels('1i')

        factor = dpi / 72
        master.tk.call('tk', 'scaling', 2.0)
        self.variables_for_graphs()
        self.variables_for_inputer()
        self.variables_for_graphs_menu()
        self.place_frames()
    def variables_for_graphs(self):
        self.HEIGHT = self.SCREEN_HEIGHT*(1000/1080)
        self.WIDHT = self.SCREEN_WIDHT*(1000/1920)

        self.graph_frame = tk.Frame(self.master, height=self.HEIGHT, width=self.WIDHT)
        self.graph_canvas = tk.Canvas(self.graph_frame, width=self.WIDHT, height=self.HEIGHT, highlightthickness=1,
                                      highlightbackground="white", bg="black")
        self.graph_canvas.create_line(self.WIDHT/2, 0, self.WIDHT/2, self.HEIGHT, width=2, fill="white")  # Y_axis
        self.graph_canvas.create_line(0, self.HEIGHT/2, self.WIDHT, self.HEIGHT/2, width=2, fill="white")  # X_axis
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
        self.input_frame = tk.Frame(self.master, height=self.SCREEN_HEIGHT*(580/1080),
                                    width=self.SCREEN_WIDHT*(920/1920), bg="black")
        self.Equation_list = []
        self.show_string = ''
        self.tag_string = ""
        self.inputer_objects(self.input_frame)
        self.is_negative = False
        self.adding_digites = False
        self.open_bracket = False
        self.bracket_list = []
        self.before_bracket = ""
    def variables_for_graphs_menu(self):
        self.menu_frame = tk.Frame(self.master,height = self.SCREEN_HEIGHT*(480/1080),width = self.SCREEN_WIDHT*(920/1920),bg = "black" )
        self.number = 0
        self.object_dic = {}
    def create_new_object_menu(self,string,frame,color):
        n = self.number
        self.object_dic[string] = [tk.Label(frame,bg = color),
                                   tk.Label(frame,text = string),
                                   tk.Button(frame,text = "delete",command = lambda : self.delete_row_in_menu(string)),
                                   self.number]
        self.number += 1
        self.place_menu_items()
    def place_menu_items(self):

        for id in self.object_dic:
            list = self.object_dic[id]
            list[0].place(x = 0,y = list[3]*80,height = 80,width=80)
            list[1].place(x=80, y=list[3]*80,height=80,width=760)
            list[2].place(x=840, y=list[3]*80,height = 80,width=80)
    def delete_row_in_menu(self,id):
        found = False
        dic = {}
        for id_ in self.object_dic:
            if found:
                dic[id_] = self.object_dic[id_]
                dic[id_][3] -= 1
            else:
                if id_ == id:
                    self.graph_canvas.delete(id)
                    self.graph_canvas.delete(id)
                    self.graph_canvas.update()
                    self.object_dic[id_][0].destroy()
                    self.object_dic[id_][1].destroy()
                    self.object_dic[id_][2].destroy()
                    found =True
                else:
                    dic[id_] = self.object_dic[id_]
        self.object_dic = dic
        self.number -= 1
        self.place_menu_items()
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
        self.botton_bracket_open = tk.Button(frame, text="(",command=self.open_bracket_botton_pressed)
        self.botton_bracket_open.place(x=552, y=180, width=184, height=100)
        self.botton_bracket_close = tk.Button(frame, text=")",command=self.close_bracket_botton_presses)
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
            self.y_axis_values_list_positive[n].place(x = self.SCREEN_WIDHT*(510/1980),y = self.SCREEN_HEIGHT*((n*50)/1080)-14)

        for n in range(10):
            self.y_axis_values_list_negative[n].place(x=self.SCREEN_WIDHT*(510/1980), y=self.SCREEN_HEIGHT*((((n+11) * 50))/1080) -14)
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
            self.x_axis_values_list_negative[n].place(x = self.SCREEN_WIDHT*(50*n)/1980 -8,y = self.SCREEN_HEIGHT*(510/1080))
        for n in range(9):
            self.x_axis_values_list_positive[n].place(x =  self.SCREEN_WIDHT*(50 * (n+10))/1980, y = self.SCREEN_HEIGHT*(510/1080))
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
        self.tag_string = ""
        for char in self.show_string:
            if char == "^":
                self.tag_string+="**"
            else:
                self.tag_string+=char

        self.create_new_object_menu(self.show_string,self.menu_frame,line_color)
        print(self.points_list)

        if "x" in equation and "y" in equation:
            print("yes")
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
                    pass
                    # self.graph_canvas.create_line(self.points_list[i][0] + 500,
                    #                               -1 * self.points_list[i][1] + 500,
                    #                               self.points_list[0][0] + 500,
                    #                               -1 * self.points_list[0][1] + 500,
                    #                               fill=line_color, tags=self.show_string)
                    # self.graph_canvas.update()
        else:
            print("no")
            for i in range(0, len(self.points_list)):
                try:
                    # correction for the shift in orign from tk's (0,0) to tk's (500,500)
                    self.graph_canvas.create_line(self.points_list[i][0] + 500,
                                                  -1 * self.points_list[i][1] + 500,
                                                  self.points_list[i + 1][0] + 500,
                                                  -1 * self.points_list[i + 1][1] + 500,
                                                  fill=line_color, tags=self.show_string,activewidth=5)
                    self.graph_canvas.update()
                    self.graph_frame.update()
                except:
                    self.graph_canvas.update()
        self.on_line("f")
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
    def on_line(self,cords):
        pass
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
            self.graph_canvas.delete("coords")
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
        if not self.open_bracket:
            if self.adding_digites:
                if self.is_negative:
                    num = (int(self.Equation_list.pop()) * 10 + int(botton["text"])) * -1
                    self.Equation_list.append(num)
                else:
                    num = int(self.Equation_list.pop()) * 10 + botton["text"]
                    self.Equation_list.append(num)
                show_string_new = ""
                for i in self.Equation_list:
                    if i == "power":
                        show_string_new += "**"
                    elif i == "multiply":
                        show_string_new += "*"
                    elif i == "divide":
                        show_string_new += "/"
                    elif i == "add":
                        show_string_new += "+"
                    elif i == "subtract":
                        show_string_new += "-"
                    else:
                        show_string_new += str(i)

                self.show_string = show_string_new
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
            self.before_bracket = self.show_string
        else:
            if self.adding_digites:
                if self.is_negative:
                    num = (int(self.bracket_list.pop()) * 10 + int(botton["text"])) * -1
                    self.bracket_list.append(num)
                else:
                    num = int(self.bracket_list.pop()) * 10 + botton["text"]
                    self.bracket_list.append(num)
                show_string_new = ""
                for i in self.bracket_list:
                    if i == "power":
                        show_string_new += "**"
                    elif i == "multiply":
                        show_string_new += "*"
                    elif i == "divide":
                        show_string_new += "/"
                    elif i == "add":
                        show_string_new += "+"
                    elif i == "subtract":
                        show_string_new += "-"
                    else:
                        show_string_new += str(i)
                self.show_string = self.before_bracket+"("
                self.show_string += show_string_new
            else:
                if self.is_negative:
                    num = int(botton["text"]) * -1
                    self.bracket_list.append(num)
                else:
                    num = botton["text"]
                    self.bracket_list.append(botton["text"])
                self.adding_digites = True
                self.show_string += str(num)
            self.equation_label.config(text=self.show_string)
    def power_botton_pressed(self):
        if not self.open_bracket:
            self.Equation_list.append("power")
        else:
            self.bracket_list.append("power")

        self.show_string += "**"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def divide_botton_pressed(self):
        if not self.open_bracket:
            self.Equation_list.append("divide")
        else:
            self.bracket_list.append("divide")
        self.show_string += "/"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def multiply_botton_pressed(self):
        if not self.open_bracket:
            self.Equation_list.append("multiply")
        else:
            self.bracket_list.append("multiply")
        self.show_string += "*"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def add_botton_pressed(self):
        if not self.open_bracket:
            self.Equation_list.append("add")
        else:
            self.bracket_list.append("add")
        self.show_string += "+"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def subtract_botton_pressed(self):
        if not self.open_bracket:
            self.Equation_list.append("subtract")
        else:
            self.bracket_list.append("subtract")
        self.show_string += "-"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def x_botton_pressed(self):
        if not self.open_bracket:
            self.Equation_list.append("x")
        else:
            self.bracket_list.append("x")
        self.show_string += "x"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def y_botton_pressed(self):
        if not self.open_bracket:
            self.Equation_list.append("y")
        else:
            self.bracket_list.append("y")
        self.show_string += "y"
        self.equation_label.config(text=self.show_string)
        self.adding_digites = False
    def polt_botton_pressed(self):
        self.show_on_top = self.show_string
        print(self.show_on_top,self.Equation_list)


        self.plot(self.Equation_list)

        self.Equation_list = []
        self.bracket_list = []
        self.open_bracket = False
        self.equation_label.config(text = "")
        self.show_string = ""
        self.adding_digites = False
    def delete_botton_pressed(self):
        show_string_new = ''
        found = False

        if not self.open_bracket:
            if type(self.Equation_list[-1]) == type(1):
                if self.Equation_list[-1] / 10 > 10:
                    pass
                else:
                    self.adding_digites = False
            try:
                self.Equation_list.pop()
            except:
                pass
            for i in self.Equation_list:
                if i == "power":
                    show_string_new += "**"
                elif i == "multiply":
                    show_string_new += "*"
                elif i == "divide":
                    show_string_new += "/"
                elif i == "add":
                    show_string_new += "+"
                elif i == "subtract":
                    show_string_new += "-"
                else:
                    show_string_new += str(i)

            self.show_string = show_string_new
            self.equation_label.config(text=self.show_string)
        else:
            self.before_bracket = ""
            for i in self.Equation_list:
                if i == "power":
                    self.before_bracket += "**"
                elif i == "multiply":
                    self.before_bracket += "*"
                elif i == "divide":
                    self.before_bracket += "/"
                elif i == "add":
                    self.before_bracket += "+"
                elif i == "subtract":
                    self.before_bracket += "-"
                else:
                    self.before_bracket += str(i)
            self.before_bracket += '('
            try:
                if type(self.bracket_list[-1]) == type(1):
                    if self.bracket_list[-1] / 10 > 10:
                        pass
                    else:
                        self.adding_digites = False
            except:
                pass
            try:
                self.bracket_list.pop()
            except:
                self.open_bracket = False
            for i in self.bracket_list:
                if i == "power":
                    show_string_new += "**"
                elif i == "multiply":
                    show_string_new += "*"
                elif i == "divide":
                    show_string_new += "/"
                elif i == "add":
                    show_string_new += "+"
                elif i == "subtract":
                    show_string_new += "-"
                else:
                    show_string_new += str(i)
            self.show_string = self.before_bracket
            self.show_string += show_string_new
            self.equation_label.config(text=self.show_string)
    def negative_botton_pressed(self):
        if self.is_negative:
            self.is_negative = False
            self.botton_num_negative.config(bg=self.botton_y["bg"],fg="black")
        else:
            self.is_negative = True
            self.botton_num_negative.config(bg = "light gray",fg="black")
        self.adding_digites = False
    def open_bracket_botton_pressed(self):
        self.adding_digites = False

        self.open_bracket = True
        self.show_string += "("
        self.equation_label.config(text=self.show_string)
    def close_bracket_botton_presses(self):
        self.open_bracket = False
        self.show_string += ")"
        self.adding_digites = False
        self.equation_label.config(text=self.show_string)
        self.Equation_list.append(self.bracket_list)
        self.bracket_list = []
    def place_frames(self):
        self.graph_frame.place(x=0,y=0)
        self.input_frame.place(x=1000, y=450)
        self.menu_frame.place(x = 1000, y= 0)

if __name__ == "__main__":
    root = tk.Tk()
    root.config(bg="black")
    main = Main(root)
    root.mainloop()