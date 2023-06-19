## Sudoku Game ## 

from tkinter import *
import numpy as np 
import random

class Sudoku : 
    def __init__(self):

        ## Create Sudoku game rules ## 

        ## Create UI in windows ##
        windows = Tk()
        windows.title(" Sudoku GUI ")

        frame1 = Frame(windows)
        frame1.pack()

        ## 創建 9 X 9 的空格
        self.cells = []
        for i in range(9):
            self.cells.append([])
            for j in range(9):
                self.cells[i].append(StringVar())

        for i in range(9):
            numbers = self.generate_number()
            for j in range(9):
                self.cells[i][j].set(numbers[j])
        
        for i in range(9):
           for j in range(9):
                Entry(frame1, width = 4, justify = RIGHT,
                      textvariable = self.cells[i][j]).grid(row = i, column = j) 
                
        frame2 = Frame(windows)
        frame2.pack()
        btSolve = Button(frame2, text = " Solve ", command = self.Slove).grid(row = 1 , column = 1)
        btClear = Button(frame2, text = " Clear ", command = self.Clear).grid(row = 1, column = 2)
        

        windows.mainloop()

    def generate_number(self):
        numbers = random.sample(range(1, 10), 9)
        return numbers
    
    def Clear(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].set("")

    def Slove(self):
        print("solve")
        
Sudoku()