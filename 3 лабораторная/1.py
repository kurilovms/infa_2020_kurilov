import turtle
from random import *

turtle.shape('turtle')
turtle.speed(0)
for i in range(1000):
    turtle.forward(randint(0,50))
    turtle.left(randint(0,360))
