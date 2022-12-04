import tkinter as tk
from calculator import Calculator as Cal
import pyautogui as pa
import random as r

class Graph_frame:
    def __init__(self,master = None):
        self.master = master
        self.HEIGHT = 1000
        self.WIDHT = 1000
        self.coords_label = tk.Label(self.master, bg="white")
        master.geometry(str(self.master.winfo_screenwidth()) + 'x' + str(self.master.winfo_screenheight()))
        master.state('zoomed')
        self.canvas = tk.Canvas(master, width=self.WIDHT, height=self.HEIGHT,highlightthickness=1,
                                highlightbackground="white",bg = "black")
        print(self.master.winfo_screenheight())
        self.canvas.create_line(500,0,500,1000,width=2,fill = "white") #Y_axis
        self.canvas.create_line(0,500,1000,500, width=2,fill = "white") #X_axis
        self.hex_list = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']
        self.y_axis_values()
        self.x_axis_values()
        self.vertical_grid()
        self.horizontal_grid()
        self.canvas.place(x = 0,y = 0)
        self.place_coords_label()
        self.input_taker()
    def vertical_grid(self):
        for i in range(0,1000,50):
            if i == 500:
                pass
            else:
                self.canvas.create_line(i,0,i,1000,width=0.01,fill="gray")
    def horizontal_grid(self):
        for i in range(0,1000,50):
            if i == 500:
                pass
            else:
                self.canvas.create_line(0,i,1000,i,fill="gray")
    def y_axis_values(self):
        self.y_axis_values_list_positive = [tk.Label(self.master,text = i,bg = "black",fg = "white") for i in range(10,-1,-1)]
        self.y_axis_values_list_negative = [tk.Label(self.master,text = i,bg = "black",fg = "white") for i in range(-1,-11,-1)]
        for n in range(11):
            self.y_axis_values_list_positive[n].place(x = 510,y = n*50-10)

        for n in range(10):
            self.y_axis_values_list_negative[n].place(x=510, y=((n+11) * 50)-14)
    def x_axis_values(self):
        self.x_axis_values_list_positive = [tk.Label(self.master, text=i, bg="black", fg="white") for i in
                                            range(1,10)]
        self.x_axis_values_list_negative = [tk.Label(self.master, text=i, bg="black", fg="white") for i in
                                            range(-10,0)]
        for n in range(10):
            self.x_axis_values_list_negative[n].place(x = 50*n -8,y = 510)
        for n in range(9):
            self.x_axis_values_list_positive[n].place(x = (50 * (n+10)) +40, y = 510)
    def calculate(self):
        self.cal = Cal(self.equation, 400, 50)
        self.points_list = self.cal.solve()
    def plot(self,equation):
        self.equation =equation
        self.calculate()
        line_color = self.random_color()
        for i in range(0, len(self.points_list)):
            try:
                self.canvas.create_line(self.points_list[i][0]+500,
                    -1*self.points_list[i][1]+500,
                    self.points_list[i+1][0]+500,
                    -1*self.points_list[i+1][1]+500,fill = line_color)
            except:
                self.canvas.update()
    def on_canvas(self,cords):
        if cords[0] <1000 and cords[1] <1000:
            return True
        else:
            return False
    def place_coords_label(self):
        self.mouse = pa.position()
        self.mouse_coords = [self.mouse.x, self.mouse.y]
        if self.on_canvas(self.mouse_coords):
            self.canvas.delete("coords")
            self.canvas.create_text(self.mouse_coords[0]+20,self.mouse_coords[1] - 50,
                                    text=str((self.mouse_coords[0] - 500)/50)+","+str(-1*((self.mouse_coords[1]-30) - 500)/50),
                                    fill = 'white',
                                    tag = "coords")
        else:
            pass
        self.master.after(1,self.place_coords_label)
    def random_color(self):
        colour_code = "#"
        for i in range(6):
            colour_code += r.choice(self.hex_list)
        return colour_code
    def input_taker(self):
        self.input_canvas = tk.Canvas(self.master, width=self.WIDHT, height=self.HEIGHT,highlightthickness=1,
                                highlightbackground="white",bg = "black")
        self.input_canvas.place(x= self.WIDHT,y = 0)

if __name__ == "__main__":
    master = tk.Tk()
    gr = Graph_frame(master)
    # gr.plot(["x","power",2,"add",2,"multiply","x"])
    # gr.plot(["x", "power", 3, "add", 2, "multiply", "x"])
    gr.plot(["x", "power", 4, "add", 2, "multiply", "x"])
    # gr.plot(["x","power",5,"add",2,"multiply","x"])

    master.mainloop()
