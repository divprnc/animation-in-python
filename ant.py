from random import*
from turtle import  *

from base  import  vector
ant = vector(0,0)
aim = vector(2,0)       #aim is vector w defined in base

def wrap(value):
    return value

def draw():
    ant.move(aim)
    ant.x = wrap(ant.x)
    ant.y = wrap(ant.y)
    aim.move(random()  - 0.5)     #to decrease speed
    aim.rotate(random()*10 -5)    #to decrease the width of rotation
    clear()
    goto(ant.x,ant.y)
    dot(4)
    if running:
               ontimer(draw,100)  #if this is true then  this draw function will be called after every 100 milli sec .

setup(420,420,370,0)                        # width,height,startx pos ,starty pos are passes as arguments
hideturtle()
tracer(False)    #for delaying purposes
up()
running = True
draw()
done()  #to exit from turtle mode

