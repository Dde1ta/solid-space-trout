import tkinter as tk


class Inputer_frame:
    def __init__(self,master):
        self.master = master
        self.input_frame = tk.Frame(master, height=580, width=920, bg="black")
        self.objects(self.input_frame)

    def objects(self,frame):
        self.equation_label = tk.Label(frame).place(x=0, y=0,width=920,height=80)
        self.botton1 = tk.Button(frame, text=1).place(x=0, y=180,width=230,height=100)
        self.botton2 = tk.Button(frame, text=2).place(x=230, y=180,width=230,height=100)
        self.botton3 = tk.Button(frame, text=3).place(x=460, y=180,width=230,height=100)
        self.botton4 = tk.Button(frame, text=4).place(x=0, y=280,width=230,height=100)
        self.botton5 = tk.Button(frame, text=5).place(x=230, y=280,width=230,height=100)
        self.botton6 = tk.Button(frame, text=6).place(x=460, y=280,width=230,height=100)
        self.botton7 = tk.Button(frame, text=7).place(x=0, y=380,width=230,height=100)
        self.botton8 = tk.Button(frame, text=8).place(x=230, y=380,width=230,height=100)
        self.botton9 = tk.Button(frame, text=9).place(x=460, y=380,width=230,height=100)
        self.botton0 = tk.Button(frame, text=0).place(x=0, y=480,width=230,height=100)
        self.botton_divide = tk.Button(frame, text="/").place(x=690, y=180,width=230,height=100)
        self.botton1_multiply = tk.Button(frame, text="*").place(x=690, y=280,width=230,height=100)
        self.botton1_add = tk.Button(frame, text="+").place(x=690, y=380,width=230,height=100)
        self.botton1_sudtract = tk.Button(frame, text="-").place(x=690, y=480,width=230,height=100)
        self.botton1_power = tk.Button(frame, text="^").place(x=690, y=80,width=230,height=100)
        self.botton1_x = tk.Button(frame, text="x").place(x=460, y=80,width=230,height=100)
        self.botton_plot = tk.Button(frame, text="Plot").place(x=230, y=480,width=460,height=100)
        self.botton_clear = tk.Button(frame, text="Clear").place(x=0, y=80,width=230,height=100)
        self.botton_delete = tk.Button(frame, text="Delete").place(x=230, y=80,width=230,height=100)

if __name__ == "__main__":
    master = tk.Tk()
    inputerr = Inputer_frame(master)
    inputerr.input_frame.pack()
    master.mainloop()


