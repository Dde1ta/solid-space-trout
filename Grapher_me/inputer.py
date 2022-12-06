import tkinter as tk


class Inputer_frame:
    def __init__(self,master):
        self.master = master
        self.input_frame = tk.Frame(master,height = 580,width = 920,bg = "black")

    def buttons(self,frame):
        self.botton1 = tk.Button(frame,text = 1)
        self.botton2 = tk.Button(frame, text=2)
        self.botton3 = tk.Button(frame, text=3)
        self.botton4 = tk.Button(frame, text=4)
        self.botton5 = tk.Button(frame, text=5)
        self.botton6 = tk.Button(frame, text=6)
        self.botton7 = tk.Button(frame, text=7)
        self.botton8 = tk.Button(frame, text=8)
        self.botton9 = tk.Button(frame,text =9)
        self.botton0 = tk.Button(frame, text=0)
        self.botton_divide = tk.Button(frame, text="/")
        self.botton1_multiply = tk.Button(frame, text="*")
        self.botton1_add = tk.Button(frame, text="+")
        self.botton1_sudtract = tk.Button(frame, text="-")
        self.botton1_power = tk.Button(frame, text="^")
        self.botton1_x = tk.Button(frame, text="x")
        self.botton_plot = tk.Button(frame, text="Plot")


