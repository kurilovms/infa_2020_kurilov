import turtle
import math

def duga(R):
    for j in range(180):
        turtle.forward(2 * R * math.sin(math.pi/360))
        turtle.right(1)


turtle.speed(0)
turtle.shape('turtle')
r1=10
r2=4
turtle.left(90)
for i in range(10):
    duga(r1)
    duga(r2)
