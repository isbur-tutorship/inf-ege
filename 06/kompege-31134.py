# kompege-31134
        
from turtle import*
left(90)
m = 10 # масштаб
tracer(0) # рисовать моментально
screensize(900,900)


#------------  алгоритм 

# kompege-31134
# Повтори 7 [Вперёд 12 Направо 90 Вперёд 20 Направо 90]
# Поднять хвост
# Вперёд 1 Направо 90 Вперёд 10 Налево 90
# Опустить хвост
# Повтори 7 [Вперёд 66 Направо 90 Вперёд 92 Направо 90]

# down()
for _ in range(7):
    forward(12*m)
    right(90)
    forward(20*m)
    right(90)
penup()
forward(1*m)
right(90)
forward(10*m)
left(90)
pendown()
for _ in range(7):
    forward(66*m)
    right(90)
    forward(92*m)
    right(90)

#---------------

up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(x*m,y*m) # перемести в точку с коорд
        dot(4, 'red')


update() # обновить экран
done() # чтобы не закрывалось окно с черепахой