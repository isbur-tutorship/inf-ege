from turtle import *

tracer(0)
screensize(2000,2000)
s = 30

for i in range(2):
    forward(1*s)
    left(270)
    forward(16*s)
    right(90)
    
penup()

backward(4*s)
right(90)
forward(10*s)
left(90)

pendown()

for i in range(2):
    forward(17*s)
    right(90)
    forward(7*s)
    right(90)


penup()
color('red')
for x in range(-20,20):
    for y in range(-20,20):
        setpos(x*s, y*s)
        dot(3)


update()
done()