import turtle

def kvadrat(a,d1):
    turtle.pendown()
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.left(180)
    turtle.penup()
    turtle.forward(d1)
    turtle.left(90)
    turtle.forward(d1)
    turtle.left(90)

turtle.shape('turtle')
b=10
d=5
for i in range(10):
    kvadrat(b,d)
    b+=2*d
