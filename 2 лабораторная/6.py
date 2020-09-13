import turtle

def noga(l,n1):
    turtle.forward(l)
    turtle.stamp()
    turtle.backward(l)
    turtle.left(360/n1)


turtle.shape('turtle')
n=7
a=100
for i in range(n):
    noga(a,n)
