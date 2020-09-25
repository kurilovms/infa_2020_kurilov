import turtle

turtle.shape('turtle')
turtle.speed(0)
dt=1e-1
x=0
y=0
v_x=5
v_y=10
a_y=-2
for i in range(1000):
    x+=v_x*dt
    y+=v_y*dt + a_y*dt**2/2
    v_y += a_y*dt
    turtle.goto(x,y)
    if y<=0:
        v_y=abs(v_y)

