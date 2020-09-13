import turtle
import math

def poch(n,R):
    turtle.left(90-90/n)
    for i in range(n):
        turtle.forward(2*R*math.cos(math.pi/n))
        turtle.right(180 - 180/n)
        


turtle.speed(0)
turtle.shape('turtle')

poch(5,50)

turtle.penup()
turtle.goto(300,0)
turtle.pendown()

poch(11,50)
