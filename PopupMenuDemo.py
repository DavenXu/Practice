from tkinter import *

class PopupMenuDemo:
    def __init__(self):
        window = Tk()
        window.title(" PopupDemo ")

        # Set Menu 
        self.menu = Menu(window, tearoff = 0)
        self.menu.add_command(label = "Draw line", command = self.Draw_line)
        self.menu.add_command(label = "Draw circle", command = self.Draw_circle)

        self.canvas = Canvas(window , width = 500, height = 500, bg = "white")
        self.canvas.pack()
        self.canvas.bind("<Button-3>", self.poup)

        window.mainloop()

    def Draw_line(self):
        self.canvas.create_line(10, 10, 190, 190,tags = "line")

    def Draw_circle(self):
        self.canvas.create_oval(250, 250, 350, 350)

    def poup(self, event):
        self.menu.post(event.x_root, event.y_root)

PopupMenuDemo()