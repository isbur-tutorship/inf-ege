# kompege-31503
# Исполнитель Собака
from turtle import *

m = 5
tracer(0) # Чтобы не тратить время на рисование

def fd(n):
    forward(n*m)
    polygon.append(pos())

polygon = []
for i in range(6):
    fd(24)
    rt(90)
    fd(30)
    rt(90)
poly1 = polygon.copy()

up()
fd(2)
rt(90)
fd(10)
lt(90)

polygon = []
down()
for i in range(6):
    fd(75)
    rt(90)
    fd(71)
    rt(90)
poly2 = polygon.copy()


def inside(pos, poly):
    x, y = pos
    xs, ys = zip(*poly)
    return min(xs) <= x <= max(xs) and min(ys) <= y <= max(ys)

c = 0
up()
for x in range(-200,200):
    for y in range(-200, 200):
        if inside((x*m,y*m), poly1) and inside((x*m,y*m), poly2):
            c += 1
            goto(x*m, y*m)
            dot(3)
        

update()
done()
print(c)