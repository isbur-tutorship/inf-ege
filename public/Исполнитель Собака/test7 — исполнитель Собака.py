# Исполнитель Собака
from math import *

x, y = 0, 0
angle = 0 # в градусах

def fd(n):
    global x, y, polygon
    x += n * cos(radians(angle))
    y += n * sin(radians(angle))
    polygon.append((x, y))

def lt(n):
    global angle
    angle += n
    
def rt(n):
    global angle
    angle -= n

    
polygon = []
for _ in range(6):
    fd(24)
    rt(90)
    fd(30)
    rt(90)
polygon1 = polygon.copy()

fd(2)
rt(90)
fd(10)
lt(90)

polygon = []
for _ in range(6):
    fd(75)
    rt(90)
    fd(71)
    rt(90)
polygon2 = polygon.copy()


def inside(pos, poly):
    xmin = min(p[0] for p in poly)
    ymin = min(p[1] for p in poly)
    xmax = max(p[0] for p in poly)
    ymax = max(p[1] for p in poly)
    return (xmin <= pos[0] <= xmax) and (ymin <= pos[1] <= ymax)

s1ands2 = 0
for x in range(-200,2006):
    for y in range(-200, 200):
        s1ands2 += inside((x, y), polygon1) * inside((x, y), polygon2)

print(s1ands2)