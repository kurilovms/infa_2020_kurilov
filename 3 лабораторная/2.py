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
            turtle.goto(i[0]+n*100,i[1])

turtle.shape('turtle')
turtle.color('blue')
l0=['pd',(50,0),(50,-100),(0,-100),(0,0),'pu',(100,0)]
l1=['pu',(0,-50),'pd',(50,0),(50,-100),'pu',(100,0)]
l2=['pd',(50,0),(50,-50),(0,-100),(50,-100),'pu',(100,0)]
l3=['pd',(50,0),(0,-50),(50,-50),(0,-100),'pu',(100,0)]
l4=['pd',(0,-50),(50,-50),(50,0),(50,-100),'pu',(100,0)]
l5=['pd',(50,0),(0,0),(0,-50),(50,-50),(50,-100),(0,-100),'pu',(100,0)]
l6=['pu',(50,0),'pd',(0,-50),(50,-50),(50,-100),(0,-100),(0,-50),'pu',(100,0)]
l7=['pd',(50,0),(0,-50),(0,-100),'pu',(100,0)]
l8=['pd',(50,0),(50,-100),(0,-100),(0,0),(0,-50),(50,-50),'pu',(100,0)]
l9=['pd',(50,0),(50,-50),(0,-100),(50,-50),(0,-50),(0,0),'pu',(100,0)]

ris(0,l1)
ris(1,l4)
ris(2,l1)
ris(3,l7)
ris(4,l0)
ris(5,l0)
