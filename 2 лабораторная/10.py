import turtle
import math

def okrug(R):
    for j in range(360):
        turtle.forward(2 * R * math.sin(0.5))
        turtle.left(1)


turtle.speed(0)
turtle.shape('turtle')
a=1
for i in range(6):
    okrug(a)
    turtle.right(60)
