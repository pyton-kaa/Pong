from turtle import Turtle, Screen
from time import sleep
import random

from table import Table
from pad import Pad
from ball import Ball
from scoreboard import Scoreboard

HEIGHT = 500
WIDTH = 800
LENGTH = 100

table = Table()
table.set_screen()
table.paint_table()

left_pad = Pad()
left_pad.set_side('left')

right_pad = Pad()
right_pad.set_side('right')

ball = Ball()
ball.set_pad('left')

scoreboard = Scoreboard()

table.screen.update()

def start_round():
    global round_is_on
    round_is_on = True

pads = {'left': left_pad, 'right': right_pad}

def bounce(ball, pads):
    if ball.is_in() != 'in':
        ydist = ball.ycor() - pads[ball.is_in()].ycor()
        if abs(ydist) < 60:
            ball.vx *= -1
            ball.vy = ydist / 40
            ball.step += 1

        else:
            ball.fall()
            global round_is_on
            round_is_on = False
            if ball.is_in() == 'left':
                scoreboard.point_right()
            elif ball.is_in() == 'right':
                scoreboard.point_left()
            scoreboard.update()
            table.screen.update()
            sleep(2)

table.screen.onkeypress(start_round, 'space')

table.screen.onkeypress(left_pad.move_up, "w")
table.screen.onkeypress(left_pad.move_down, "s")
table.screen.onkeypress(right_pad.move_up, "Up")
table.screen.onkeypress(right_pad.move_down, "Down")

round_is_on = False
while max(scoreboard.left_score, scoreboard.right_score) < 11:
    round_parity = (scoreboard.left_score + scoreboard.right_score)%2
    ball.prepare(round_parity, pads)
    while round_is_on == False:
        sleep(0.02)
        if ball.ycor != list(pads.values())[round_parity].ycor():
            ball.sety(list(pads.values())[round_parity].ycor())
        table.screen.update()

    while round_is_on:
        sleep(0.02)
        ball.move()
        ball.bounce_wall()
        bounce(ball, pads)
        table.screen.update()
    ball.recover()

scoreboard.result()



table.screen.exitonclick()