import turtle

def ris(n,a):
    turtle.penup()
    turtle.goto(n*100,0)
    for i in a:
        if i== 'pd':
            turtle.pendown()
        elif i == 'pu':
            turtle.penup()
        else:
            i=i.split(',')
            turtle.goto(int(i[0])+n*100,int(i[1]))

turtle.shape('turtle')
turtle.color('blue')

l=[]
j=0
with open('input.txt') as file:
    for line in file:
        l.append(line.split())
        j+=1

ris(0,l[1])
ris(1,l[4])
ris(2,l[1])
ris(3,l[7])
ris(4,l[0])
ris(5,l[0])
