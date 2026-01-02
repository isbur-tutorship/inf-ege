from turtle import *
left(90)
m = 10 # масштаб
tracer(0) # рисовать моментально
screensize(1920,2000)

def mfd(n):
    fd(n*m)
def bwd(n):
    backward(n*m)
#------------  алгоритм 
x = 30

down()
color("green")
for _ in range(4):
    mfd(x)
    right(90)
    mfd(48)
    right(90)
    
up()
mfd(27)
rt(90)
mfd(24)
lt(90)

down()
color("blue")
for _ in range(4):
    mfd(29)
    right(90)
    bwd(18)
    right(90)

#---------------

up()
for x in range(0,70):
    for y in range(0,70):
        goto(x*m,y*m) # перемести в точку с коорд
        dot(4, 'red')


update() # обновить экран
done() # чтобы не закрывалось окно с черепахой