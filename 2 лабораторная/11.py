import turtle
import math

def okrug_left(R):
    for j in range(360):
        turtle.forward(2 * R * math.sin(math.pi/360))
        turtle.left(1)

def okrug_right(R):
    for j in range(360):
        turtle.forward(2 * R * math.sin(math.pi/360))
        turtle.right(1)


turtle.speed(0)
turtle.shape('turtle')
a=10
d=5
turtle.left(90)
for i in range(10):
    okrug_left(a)
    okrug_right(a)
    a+=d
