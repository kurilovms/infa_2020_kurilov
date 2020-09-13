import turtle
import math

def maloe(phi1,delta_phi1,k1):
    x=k1*(phi1 + delta_phi1)*math.cos(phi1 + delta_phi1)
    y=k1*(phi1 + delta_phi1)*math.sin(phi1 + delta_phi1)
    turtle.goto(x, y)

turtle.shape('turtle')
phi=0
delta_phi=0.1
k=0.5
for i in range(1000):
    maloe(phi,delta_phi,k)
    phi+=delta_phi
