from turtle import Turtle

LENGTH = 100
HEIGHT = 500
WIDTH = 800
STEP = 5

class Pad(Turtle):

    def __init__(self):
        super().__init__()
        self.side = None
        self.shape('square')
        self.shapesize(1,5,1)
        self.penup()
        self.pencolor('yellow')
        self.fillcolor('white')
        self.seth(90)
        self.sety(-10)

    def set_side(self, side):
        self.side = side
        if side == 'left':
            self.setx(-WIDTH/2 - 10)
        elif side == 'right':
            self.setx(WIDTH/2 + 10)

    def move_up(self):
        if self.ycor() < (HEIGHT - LENGTH) / 2 - 10:
            self.seth(90)
            self.fd(8)
            # print('Up!')
    
    def move_down(self):
        if self.ycor() > (LENGTH - HEIGHT) / 2 - 10:
            self.seth(270)
            self.fd(8)

