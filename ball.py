from turtle import Turtle
import random

HEIGHT = 500
WIDTH = 800

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.fillcolor('white')
        self.pencolor('yellow')
        self.shape('circle')
        self.sety(-10)
        self.vx = 1
        self.vy = 1
        self.step = 10

    def move(self):
        self.setx(self.xcor() + self.step * self.vx)
        self.sety(self.ycor() + self.step * self.vy)

    def set_pad(self, side):
        if side == 'left':
            self.setx(-WIDTH/2 + 10)
        elif side == 'right':
            self.setx(WIDTH/2 - 10)

    def bounce_wall(self):
        if self.ycor() > HEIGHT/2 - 20 - self.step * self.vy or self.ycor() < -HEIGHT/2 - self.step * self.vy:
            self.vy *= -1
    
    def fall(self):
        self.fillcolor('red')

    def recover(self):
        self.fillcolor('white')

    def is_in(self):
        if self.xcor() < -WIDTH/2 + 15:
            return 'left'
        elif self.xcor() > WIDTH/2 - 15:
            return 'right'
        else:
            return 'in'
    
    def prepare(self, parity, pads):
        self.vx = 1 - 2 * parity
        self.vy = random.randint(-30,30)/20
        self.sety(list(pads.values())[parity].ycor())
        self.setx(self.vx * (10-WIDTH/2))
        self.step = 10
