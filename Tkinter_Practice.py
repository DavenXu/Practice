from tkinter import *

class ProcessButtonEvent :
     def __init__(self) :
          window = Tk()
          window.title(" Daven Xu Demo ")

          frame1 = Frame(window)
          frame1.pack()

          self.v1 = IntVar()
          cbtBold = Checkbutton(frame1, text = " Bold ", variable= self.v1, command = self.processCheckButton)

          self.v2 = IntVar()
          rbRed = Radiobutton(frame1, text= " Red ", variable= self.v2, value = 1, command = self.processRadioButton)
          rbYellow = Radiobutton(frame1, text= " Yellow ", variable= self.v2, value = 2  ,command = self.processRadioButton)
          cbtBold.grid(row = 1 ,column = 1 )
          rbRed.grid(row = 1 ,column = 2 )
          rbYellow.grid(row = 1 ,column = 3 )

          frame2 = Frame(window)
          frame2.pack()
          label = Label(frame2, text = "Enter you name : ")
          self.name = StringVar()
          entryNmae = Entry(frame2, textvariabl = self.name)
          btGetName = Button(frame2, text = " Get name ", command = self.processButton)
          message = Message(frame2 , text = " It is a widgets demo ")
          label.grid(row = 1 , column = 1)
          entryNmae.grid(row = 1 , column = 2)
          btGetName.grid(row = 1 , column = 3)
          message.grid(row = 1 , column = 4) 

          text = Text(window)
          text.pack()
          text.insert('1.0'," 我也很想他 ")
          text.insert('2.0'," 我們都一樣 ")
          text.insert('3.0'," 在你的心上 ")
          text.insert('4.0'," 曾到翅膀 ")
          window.mainloop()
     


     def processCheckButton(self):
          print("Checked button is " + ("Checked " if self.v1.get() else "Unchecked "))

     def processRadioButton(self):
          print(("RED" if self.v2.get() == 1 else "Yellow") + " is selected")

     def processButton(self):
          print("Your name is " + self.name.get())

ProcessButtonEvent()