import turtle

def iteration(a1,d1):
    for i in range(2):
        turtle.forward(a1)
        turtle.left(90)
    for i in range(2):
        turtle.forward(a1 + d1)
        turtle.left(90)        
    

turtle.shape('turtle')

a=8
d=4
for i in range(10):
    iteration(a,d)
    a+=2*d
