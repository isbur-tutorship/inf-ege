# reshuege-47313
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
for _ in range(10):
    fd(9)
    rt(90)
    fd(2)
    rt(90)
polygon1 = polygon.copy()


# reshuege-84700
#rt(180)
#polygon = []
#for _ in range(9):
    #fd(66)
    #lt(90)
    #fd(100)
    #lt(90)
#polygon1 = polygon.copy()

#fd(27)
#lt(90)
#fd(41)
#rt(90)

#polygon = []
#for _ in range(9):
    #fd(120)
    #rt(90)
    #fd(99)
    #rt(90)
#polygon2 = polygon.copy()


#def inside(pos, poly):
    #xmin = min(p[0] for p in poly)
    #ymin = min(p[1] for p in poly)
    #xmax = max(p[0] for p in poly)
    #ymax = max(p[1] for p in poly)
    #return (xmin <= pos[0] <= xmax) and (ymin <= pos[1] <= ymax)

def inside(pos, poly):
    x, y = pos
    xs, ys = zip(*poly)
    return min(xs) <= x <= max(xs) and min(ys) <= y <= max(ys)

s1ands2 = 0
for x in range(-200,200):
    for y in range(-200, 200):
        #s1ands2 += inside((x, y), polygon1) * inside((x, y), polygon2)
        s1ands2 += inside((x,y), polygon)

print(s1ands2)