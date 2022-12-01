import tkinter as tk
from calculator import Calculator as Cal

class Graph:
    def __init__(self,master = None):
        self
        self.cal = Cal(["x","power",3,"add",5,"multiply","x","power",2,"add",3,"multiply","x","add",5],400,40)
        self.master = master
        self.HEIGHT = 700
        self.WIDHT = 1200
        master.geometry(str(self.WIDHT) + 'x' + str(self.HEIGHT))
        self.canvas = tk.Canvas(master, width=self.WIDHT, height=self.HEIGHT,highlightthickness=1,
                                highlightbackground="black")
        self.canvas.create_line(400,0,400,700,width=5)
        self.canvas.create_line(0,360,800,360, width=5)
        self.vertical_grid()
        self.horizontal_grid()
        self.polt()
        self.canvas.pack()

    def vertical_grid(self):
        for i in range(0,840,40):
            if i == 400:
                pass
            else:
                self.canvas.create_line(i,0,i,800,width=0.01,fill="gray")
    def horizontal_grid(self):
        for i in range(0,800,40):
            if i == 360:
                pass
            else:
                self.canvas.create_line(0,i,800,i,fill="gray")

    def calculate(self):
        self.points_list = self.cal.solve()
        print(self.points_list)
    def polt(self):
        self.calculate()
        for i in range(0, len(self.points_list)):
            try:
                self.canvas.create_line(self.points_list[i][0]+400,
                    -1*self.points_list[i][1]+360,
                    self.points_list[i+1][0]+400,
                    -1*self.points_list[i+1][1]+360)
                print(i,len(self.points_list))
            except:
                self.canvas.update()


if __name__ == "__main__":
    master = tk.Tk()
    gr = Graph(master)
    master.mainloop()