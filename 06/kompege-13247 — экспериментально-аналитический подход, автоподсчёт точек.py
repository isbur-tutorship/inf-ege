"""
У черепахи оси координат направлены Ох вправо, а Оу вверх.
У холста Ох также направлена вправо, а Оу вниз.
"""
"""
kompege #13247
"""

from turtle import *

# Fullscreen the canvas
tracer(False)
screen = Screen()
screen.setup(1.0, 1.0)

# Begin!


# t.goto(-start, start)





# Рисуем
print("Перед первым прямоугольником", pos())

pendown()
for _ in range(2):
    forward(12)
    print("Вершина 1.1", pos())
    right(90)
    fd(19)
    print("Вершина 1.2", pos())
    rt(90)

# (-35, -5) вверх
penup()
fd(4)
rt(90)
fd(6)
lt(90)

print("Перед вторым прямоугльником", pos())
pendown()
for _ in range(32):
    fd(12)
    print("Вершина 2.1", pos())
    rt(90)
    fd(6)
    print("Вершина 2.2", pos())
    rt(90)

#Перед первым прямоугольником (0.00,0.00)
#Вершина 1.1 (12.00,0.00)
#Вершина 1.2 (12.00,-19.00)
#Вершина 1.1 (0.00,-19.00)
#Вершина 1.2 (-0.00,0.00)
#Перед вторым прямоугльником (4.00,-6.00)
#Вершина 2.1 (16.00,-6.00)
#Вершина 2.2 (16.00,-12.00)
#Вершина 2.1 (4.00,-12.00)
#Вершина 2.2 (4.00,-6.00)


def check(x, y: int):
    return y >= -12 and y <= -6 and x >= 4 and x <= 12


counter = 0
for i in range(-500, 500):
    for j in range(-500, 500):
        if check(i, j):
             counter += 1

print(counter)


screen.mainloop()
