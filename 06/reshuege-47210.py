from turtle import *
left(90)
m = 30 # масштаб
tracer(0) # рисовать моментально
screensize(900,900)


#------------  алгоритм 
down()
for _ in range(7):
    forward(10*m)
    right(120)


#---------------

up()
for x in range(-m,m):
    for y in range(-m,m):
        goto(x*m,y*m) # перемести в точку с коорд
        dot(4, 'red')


update() # обновить экран
done() # чтобы не закрывалось окно с черепахой