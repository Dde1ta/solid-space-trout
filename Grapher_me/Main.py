import tkinter as tk
from potter import Graph_frame
from inputer import Inputer_frame

if __name__ == "__main__":
    master = tk.Tk()
    master.geometry(str(master.winfo_screenwidth()) + 'x' + str(master.winfo_screenheight()))
    master.state('zoomed')
    ip = Inputer_frame(master)
    ip.input_frame.place(x=1000, y=450)
    master.mainloop()