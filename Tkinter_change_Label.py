from tkinter import *

class ChangeLabelDemo:
     def __init__(self) :
        window = Tk()
        window.title("Change Label Demo")

        frame1 = Frame(window)
        frame1.pack()
        self.label1 = Label(frame1, text = " Program is fun ")
        self.label1.pack()

        frame2 = Frame(window)
        frame2.pack()
        self.label2 = Label(frame2, text = " Enter text ")
        self.msg = StringVar()
        entry = Entry(frame2 ,textvariable =self.msg)
        entry.bind('<Enter>', self.processEnter)        #  按下Enter之後回傳至self.processEnter
        btChangeText  = Button(frame2, text = " Change Color ", )
        self.v1 = StringVar()
        rbRED = Radiobutton(frame2, text = "RED", bg = "red", variable = self.v1 \
                            , value = "R", command = self.processRadioButton)
        rbYellow = Radiobutton(frame2, text = "Yellow", bg = "yellow", variable = self.v1 \
                            , value = "Y", command = self.processRadioButton)
        self.label2.grid(row = 1, column = 1)
        entry.grid(row = 1, column = 2)
        btChangeText.grid(row = 1, column = 3)
        rbRED.grid(row = 1, column = 4)
        rbYellow.grid(row = 1, column = 5)
        
        window.mainloop()

     def processRadioButton(self):
         if self.v1.get() == "R":
             self.label1["fg"] = "red"
         elif self.v1.get() == "Y":
             self.label1["fg"] = "Yellow"

     def processButton(self):
         self.label2[" text "] = self.msg.get()

     def processEnter(self,event):
         text = self.msg.get()
         print(text)

ChangeLabelDemo()