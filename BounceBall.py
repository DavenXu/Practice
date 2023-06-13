from tkinter import *
import random 

def getRandomColor():
    color = '#'
    for j in range(6):
        color += toHexChar(random.randint(0, 15))
    return color

def toHexChar(hexvalue):
    if 0 <= hexvalue <= 9 :
        return chr(hexvalue + ord('0'))
    else :
        return chr(hexvalue - 10 + ord('0'))

class Ball: 
    def __init__(self):
        self.x = 0 
        self.y = 0
        self.dx = 2
        self.dy = 2 
        self.radius = 3
        self.color = getRandomColor()

class BounceBalls:
    def __init__(self):
        self.ball = []

        window = Tk()
        window.title("Bounce Ball")

        self.width = 350
        self.height = 150
        self.canvas = Canvas(window, bg = "white", 
                             width = self.width, height = self.height)
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()
        btStop = Button(frame1, text = "Stop", command = self.stop).grid(row = 1, column = 1)   
        btResume = Button(frame1, text = "Resume", command = self.resume).grid(row = 1, column = 2)
        btAdd = Button(frame1, text = "Add", command = self.add).grid(row = 1, column = 3)
        btRemove = Button(frame1, text = "Remove", command = self.remove).grid(row = 1, column = 4)

        ## 參數設定位置 ##
        self.sleepTime = 100
        self.isStopped = False
        self.animate()
        window.mainloop()

    def stop(self):
        self.isStopped = True

    def resume(self):
        self.isStopped = False
    
    def add(self):
        self.ball.append(Ball())

    def remove(self):
        self.ball.pop()

    def animate(self):
        while not self.isStopped:
            self.canvas.after(self.sleepTime)
            self.canvas.update()
            self.canvas.delete("ball")

            for ball in self.ball:
                self.redisPlayBall(ball)

    def redisPlayBall(self, ball):
        if ball.x > self.width or ball.x < 0:
            ball.dx = -ball.dx

        if ball.y > self.height or ball.y < 0:
            ball.dy = -ball.dy

        ball.x += ball.dx
        ball.y += ball.dy
        self.canvas.create_oval(ball.x - ball.radius, 
                                ball.y - ball.radius, ball.x + ball.radius,
                                ball.y + ball.radius, fill = ball.color ,tags = "ball")

BounceBalls()