from random import randint
import turtle

turtle.penup()
turtle.speed(0)
turtle.goto(-300,-300)
turtle.pendown()
turtle.width(5)
turtle.goto(300,-300)
turtle.goto(300,300)
turtle.goto(-300,300)
turtle.goto(-300,-300)
turtle.penup()
turtle.goto(-350,-300)
turtle.color('white')


number_of_turtles = 10
steps_of_time_number = 1000

l=[]
dt=1e-2

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for j in range(number_of_turtles):
    pool[j].penup()
    pool[j].speed(0)
    x=randint(-300,300)
    y=randint(-300,300)
    v_x=randint(-400,400)
    v_y=randint(-400,400)
    l.append([x,y,v_x,v_y,True])

for i in range(steps_of_time_number):
    for j in range(number_of_turtles):
        v_x=l[j][2]
        v_y=l[j][3]
        l[j][0]+=v_x*dt
        l[j][1]+=v_y*dt
        pool[j].goto(l[j][0],l[j][1])
        for k in range(number_of_turtles):
            if (l[k][4]) and (k != j) and ((l[j][0]-l[k][0])**2 + (l[j][1]-l[k][1])**2 <= 100):
                l[j][2],l[k][2] = l[k][2],l[j][2]
                l[j][3],l[k][3] = l[k][3],l[j][3]
                l[k][4]=False
        if l[j][0] >= 300:
            l[j][2]=-abs(v_x)
        if l[j][0] <= -300:
            l[j][2]=abs(v_x)
        if l[j][1] >= 300:
            l[j][3]=-abs(v_y)
        if l[j][1] <= -300:
            l[j][3]=abs(v_y)
        l[j][4]=True

