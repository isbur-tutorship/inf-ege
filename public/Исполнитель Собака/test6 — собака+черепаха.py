# reshuege-47313
# Исполнитель Собака
from turtle import *

tracer(0) # Чтобы не тратить время на рисование

def fd(n):
    global polygon
    forward(n)
    polygon.append(pos())

polygon = []
for _ in range(10):
    fd(9)
    rt(90)
    fd(2)
    rt(90)
# polygon1 = polygon.copy() — нужно сделать перед обнулением polygon (если таковое требуется)

def inside(pos, poly):
    x, y = pos
    xs, ys = zip(*poly)
    return min(xs) <= x <= max(xs) and min(ys) <= y <= max(ys)

c = 0
for x in range(-200,200):
    for y in range(-200, 200):
        c += inside((x,y), polygon)

print(c)

        #s1ands2 += inside((x, y), polygon1) * inside((x, y), polygon2) — если пересечение