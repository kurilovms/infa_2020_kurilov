import turtle
import math

def duga(R):
    for j in range(45):
        turtle.forward(2 * R * math.sin(math.pi/90))
        turtle.left(4)


turtle.speed(0)
turtle.shape('turtle')


turtle.begin_fill()
duga(50)
duga(50)
turtle.color('yellow')
turtle.end_fill()

turtle.color('black')
turtle.penup()
turtle.goto(0,50)
turtle.left(90)
turtle.pendown()
turtle.width(5)
turtle.backward(20)

turtle.penup()
turtle.goto(-30,50)
turtle.pendown()
turtle.color('red')
turtle.left(180)
duga(30)

turtle.penup()
turtle.width(1)
turtle.goto(-30,70)
turtle.color('black')
turtle.pendown()
turtle.left(180)
turtle.begin_fill()
duga(5)
duga(5)
turtle.color('blue')
turtle.end_fill()

turtle.penup()
turtle.width(1)
turtle.goto(30,70)
turtle.color('black')
turtle.pendown()
turtle.left(180)
turtle.begin_fill()
duga(5)
duga(5)
turtle.color('blue')
turtle.end_fill()

turtle.penup()
turtle.goto(100,100)
