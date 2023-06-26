from turtle import Turtle, Screen
WIDTH = 800
HEIGHT = 500


class Table():
    def __init__(self):
        self.screen = self.set_screen()
        self.screen.tracer(0)
        self.screen.listen()
        self.label_players()

    def set_screen(self):
        table = Screen()
        table.setup(width = WIDTH + 60, height = HEIGHT + 60)
        table.bgcolor('black')
        return(table)

    def paint_table(self):
        painter = Turtle()
        painter.ht()
        painter.penup()
        painter.pensize(3)
        painter.pencolor('white')
        painter.fillcolor('#005500')
        painter.goto(-WIDTH/2, HEIGHT/2 - 10)
        painter.pendown()
        painter.begin_fill()
        painter.goto(WIDTH/2, HEIGHT/2 - 10)
        painter.goto(WIDTH/2, -HEIGHT/2 - 10)
        painter.goto(-WIDTH/2, -HEIGHT/2 - 10)
        painter.goto(-WIDTH/2, HEIGHT/2 - 10)
        painter.end_fill()
        painter.penup()
        painter.goto(0, HEIGHT/2 - 5)
        painter.seth(270)
        for n in range(int(HEIGHT/20)):
            painter.fd(10)
            painter.pendown()
            painter.fd(10)
            painter.penup()
        self.screen.update()
     
    def label_players(self):
        label = Turtle()
        label.ht()
        label.penup()
        label.color('white')
        label.goto(-WIDTH/2, HEIGHT/2 + 5)
        label.write('Player 1', font = ('Courier', 18, 'normal'), align = 'left')
        label.sety(HEIGHT/2-10)
        label.write('Controls: W/S', font = ('Courier', 10, 'normal'), align = 'left')
        label.goto(WIDTH/2, HEIGHT/2 + 5)
        label.write('Player 2', font = ('Courier', 18, 'normal'), align = 'right')
        label.sety(HEIGHT/2-10)
        label.write('Controls: Up/Down', font = ('Courier', 10, 'normal'), align = 'right')