from turtle import *

tracer(0)
screensize(2000,2000)

k = 5

# Направо 180
right(180)
# Повтори 9 [Вперёд 59 Налево 90 Вперёд 84 Налево 90]
for i in range(9):
    forward(59*k)
    left(90)
    forward(84*k)
    left(90)
# Поднять хвост
up()
# Вперёд 18 Налево 90 Вперёд 38 Направо 90
forward(18*k)
left(90)
forward(38*k)
right(90)
# Опустить хвост
down()
# Повтори 9 [Вперёд 120 Направо 90 Вперёд 99 Направо 90]
for i in range(9):
    forward(120*k)
    right(90)
    forward(99*k)
    right(90)

update()
done()