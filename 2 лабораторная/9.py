import turtle
import math

def pochmak(n,R):
    turtle.penup()
    turtle.goto(R,0)
    turtle.pendown()
    alpha_rad=math.pi/n
    alpha_grad=180/n
    l=2*R*math.sin(alpha_rad)
    turtle.left(90 + alpha_grad)
    for i in range(n):
        turtle.forward(l)
        turtle.left(2*alpha_grad)
    turtle.right(90 + alpha_grad)    
        
    

turtle.shape('turtle')
a=8
d=4
for i in range(10):
    pochmak(i+3,a)
    a+=2*d
    
