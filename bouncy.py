from random import *
from turtle import *
from base import vector

def value():

    return(3+random()*2)*choice([-1,1])

ball = vector(0,0)
aim = vector(value(),value())

def draw():
    ball.move(aim)
    x = ball.x
    y = ball.y

    if x < -200 or x > 200:
        aim.x = -aim.x
        
         if y < -200 or y> 200:
            aim.y = -aim.y

            clear()
            goto(x,y)
            dot(10,'blue')
            ontimer(draw,50)

            setup(420,420,370,0)
            hideturtle()
            tracer(False)
            up()
            draw()
            done()
