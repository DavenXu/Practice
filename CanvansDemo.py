from tkinter import *

class canvansDemo:
    def __init__(self):
        window = Tk()
        window.title("Canvans Demo")
        self.canvas = Canvas(window, width=500, height=500, bg="white")
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()
        btRectangle = Button(frame1, text = "Rectangle", command = self.displayRect)
        btOval = Button(frame1, text = "Oval", command = self.displayOval )
        btClear = Button(frame1, text = "Clear", command = self.claerCanvas)
        btTri = Button(frame1, text = "Triangle", command = self.displayTriangle)

        btRectangle.grid(row=1 , column=1)
        btOval.grid(row = 1, column = 2)
        btClear.grid(row =1 ,column = 3)
        btTri.grid(row = 1 , column = 4)

        window.mainloop()

    def displayRect(self):
        self.canvas.create_rectangle(10, 10, 190, 190 , tags= "Rect")

    def displayOval(self):
        self.canvas.create_oval(10, 10, 190, 190, fill = "blue" , tags = "Oval")
    
    def displayTriangle(self):
        self.canvas.create_polygon(10,10,10,100,50,50, tags = "Triangle")

    def claerCanvas(self):
        self.canvas.delete("Rect", "Oval", "Triangle")

canvansDemo()
