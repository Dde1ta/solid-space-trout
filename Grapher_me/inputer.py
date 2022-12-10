import tkinter as tk
from potter import Graph_frame


class Inputer_frame(Graph_frame):
    def __init__(self,master):
        self.show_string = ''
        self.master = master
        self.input_frame = tk.Frame(master, height=580, width=920, bg="black")
        self.objects(self.input_frame)
        self.Equation_list = []
    def objects(self,frame):
        self.equation_label = tk.Label(frame)
        self.equation_label.place(x=0, y=0,width=920,height=80)
        self.botton1 = tk.Button(frame, text=1,command=lambda :self.number_botton_pressed(self.botton1))
        self.botton1.place(x=0, y=180,width=230,height=100)
        self.botton2 = tk.Button(frame, text=2,command=lambda :self.number_botton_pressed(self.botton2))
        self.botton2.place(x=230, y=180,width=230,height=100)
        self.botton3 = tk.Button(frame, text=3,command=lambda :self.number_botton_pressed(self.botton3))
        self.botton3.place(x=460, y=180,width=230,height=100)
        self.botton4 = tk.Button(frame, text=4,command=lambda :self.number_botton_pressed(self.botton4))
        self.botton4.place(x=0, y=280,width=230,height=100)
        self.botton5 = tk.Button(frame, text=5,command=lambda :self.number_botton_pressed(self.botton5))
        self.botton5.place(x=230, y=280,width=230,height=100)
        self.botton6 = tk.Button(frame, text=6,command=lambda :self.number_botton_pressed(self.botton6))
        self.botton6.place(x=460, y=280,width=230,height=100)
        self.botton7 = tk.Button(frame, text=7,command=lambda :self.number_botton_pressed(self.botton7))
        self.botton7.place(x=0, y=380,width=230,height=100)
        self.botton8 = tk.Button(frame, text=8,command=lambda :self.number_botton_pressed(self.botton8))
        self.botton8.place(x=230, y=380,width=230,height=100)
        self.botton9 = tk.Button(frame, text=9,command=lambda :self.number_botton_pressed(self.botton9))
        self.botton9.place(x=460, y=380,width=230,height=100)
        self.botton0 = tk.Button(frame, text=0,command=lambda :self.number_botton_pressed(self.botton0))
        self.botton0.place(x=0, y=480,width=230,height=100)
        self.botton_divide = tk.Button(frame, text="/",command=self.divide_botton_pressed)
        self.botton_divide.place(x=690, y=180,width=230,height=100)
        self.botton_multiply = tk.Button(frame, text="*",command=self.multiply_botton_pressed)
        self.botton_multiply.place(x=690, y=280,width=230,height=100)
        self.botton_add = tk.Button(frame, text="+",command=self.add_botton_pressed)
        self.botton_add.place(x=690, y=380,width=230,height=100)
        self.botton_subtract = tk.Button(frame, text="-",command=self.subtract_botton_pressed)
        self.botton_subtract.place(x=690, y=480,width=230,height=100)
        self.botton_power = tk.Button(frame, text="^",command=self.power_botton_pressed)
        self.botton_power.place(x=690, y=80,width=230,height=100)
        self.botton_x = tk.Button(frame, text="x",command=self.x_botton_pressed)
        self.botton_x.place(x=460, y=80,width=230,height=100)
        self.botton_plot = tk.Button(frame, text="Plot",command = self.polt_botton_pressed)
        self.botton_plot.place(x=230, y=480,width=460,height=100)
        self.botton_clear = tk.Button(frame, text="Clear")
        self.botton_clear.place(x=0, y=80,width=230,height=100)
        self.botton_delete = tk.Button(frame, text="Delete")
        self.botton_delete.place(x=230, y=80,width=230,height=100)
    def number_botton_pressed(self,botton):
        self.Equation_list.append(botton["text"])
        self.show_string += str(botton["text"])
        self.equation_label.config(text = self.show_string)
    def power_botton_pressed(self):
        self.Equation_list.append("power")
        self.show_string += "**"
        self.equation_label.config(text=self.show_string)
    def divide_botton_pressed(self):
        self.Equation_list.append("divide")
        self.show_string += "/"
        self.equation_label.config(text=self.show_string)
    def multiply_botton_pressed(self):
        self.Equation_list.append("multiply")
        self.show_string += "*"
        self.equation_label.config(text=self.show_string)
    def add_botton_pressed(self):
        self.Equation_list.append("add")
        self.show_string += "+"
        self.equation_label.config(text=self.show_string)
    def subtract_botton_pressed(self):
        self.Equation_list.append("subtract")
        self.show_string += "-"
        self.equation_label.config(text=self.show_string)
    def x_botton_pressed(self):
        self.Equation_list.append("x")
        self.show_string += "x"
        self.equation_label.config(text=self.show_string)
    def polt_botton_pressed(self):

        self.plot(self.Equation_list)
        self.Equation_list = []

    def place_frame_input(self,x,y):
        self.input_frame.place(x = x,y = y)
