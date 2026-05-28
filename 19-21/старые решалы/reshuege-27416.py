import sys
sys.setrecursionlimit(1500) # если минога камней
# Оптимизация рекурсии: мы запоминаем результаты вызовов от определённых значений
from functools import lru_cache

@lru_cache(None) # Часть магии оптимизации
def f(a, b):
    if a + b >= 77: # Условие выигрыша
        return 0

    # Перебираем все возможные ходы
    turns = [
        (a + 1, b),
        (a, b + 1),
        (a * 2, b),
        (a, b * 2)
    ]

    if any(f(*turn) == 0 for turn in turns):
        return 1

    #if any(f(*turn) == 1 for turn in turns):
    #    return 2

    if all(f(*turn) == 1 for turn in turns):
        return 2
    if any(f(*turn) == 2 for turn in turns):
        return 3
    if all(f(*turn) in (1, 3) for turn in turns):
        return 4

for s in range (1, 77):
#    if f(7, s) == 2:
#        print(s)
#        break
    if f(7, s) == 3:
        print("3", s)
    elif f(7, s) == 4:
        print("4", s)