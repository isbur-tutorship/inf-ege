# kompege-31113
# Исполнитель Собака
from turtle import *

tracer(1) # Чтобы не тратить время на рисование

def fd(n):
    forward(n)
    polygon.append(pos())

polygon = []
for _ in range(5):
    fd(29)
    rt(90)
    fd(27)
    rt(90)
poly1 = polygon.copy()
fd(3)
rt(90)
fd(9)
lt(90)
polygon = []
for _ in range(5):
    fd(72)
    rt(90)
    fd(95)
    rt(90)
poly2 = polygon.copy()
# polygon1 = polygon.copy() — нужно сделать перед обнулением polygon (если таковое требуется)

def inside(pos, poly):
    x, y = pos
    xs, ys = zip(*poly)
    return min(xs) <= x <= max(xs) and min(ys) <= y <= max(ys)

c = 0
for x in range(-200,200):
    for y in range(-200, 200):
        c += inside((x,y), poly1) and inside((x,y), poly2)

print(c)

        #s1ands2 += inside((x, y), polygon1) * inside((x, y), polygon2) — если пересечение