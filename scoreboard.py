from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.ht()
        self.penup()
        self.pencolor('white')
        self.goto(0,240)
        self.update()
    
    
    def point_left(self):
        self.left_score += 1
    
    def point_right(self):
        self.right_score += 1

    def update(self):
        self.clear()
        self.write(f'{self.left_score} : {self.right_score}', font = ('courier', 30, 'normal'), align = 'center')

    def result(self):
        self.goto(0,0)
        if self.left_score > self.right_score:
            self.write('Player 1 wins', font = ('Courier', 24, 'bold'), align = 'center')
        elif self.left_score < self.right_score:
            self.write('Player 2 wins', font = ('Courier', 24, 'bold'), align = 'center')


