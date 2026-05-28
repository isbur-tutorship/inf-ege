
> * Задание 1 из домашней работы Флеша *

## Решение через Excel:

https://docs.google.com/spreadsheets/d/1iB98T5RNAmyIp3He0m0ZHyAwhQTXvJqJ9lKNiY--d8I/edit#gid=525142007

## Excel-подобный код:

Excel-подобный код для решения задания 19:

```python
def f(n):
    a, b = 7, n
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        if max(2*i+j, i+2*j) >= 75:
            return True

for i in range(65):
    if f(i):
        print(i)
        break
```

Excel-подобный код для решения задания 20:
```python
def f(a, b):
    wins = []
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        wins.append(
            max(2*i+j, i+2*j) >= 75 and
            i + j < 75
        )
    if all(wins):
        return True

def g(a, b):
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        if f(i, j):
            return True
            
for i in range(65):
    if g(7, i):
        print(i)
```

Excel-подобный код для решения 21 задачи:
```python
def f(a, b):
    wins = []
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        wins.append(
            max(2*i+j, i+2*j) >= 75 and
            i + j < 75
        )
    if all(wins):
        return True

def g(a, b):
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        if f(i, j):
            return True

def h(a, b): # Петя
    wins = []
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        wins.append(
            g(i, j) or 
            (max(2*i+j, i+2*j) >= 75 and
                i + j < 75
            )
        )
    if all(wins):
        return True

for i in range(65):
    if h(7, i):
        print(i)
```

Excel-подобный код решения для задания 21 с использованием обобщённых функций:
```python
def Eeee(i, j):
    return max(2*i+j, i+2*j) >= 75

def Meta(a, b, condition, allOrAny = all):
    wins = []
    for i, j in (
        (a + 1, b),
        (a, b + 1),
        (a + b, b),
        (a, a + b)
    ):
        wins.append(condition(i, j))
    if allOrAny(wins):
        return True

def f(a, b):
    return Meta(a, b, lambda i, j: Eeee(i, j) and i+j < 75)

def g(a, b):
    return Meta(a, b, lambda i, j: f(i, j), any)

def h(a, b): # Петя
    return Meta(a, b, lambda i, j: g(i, j) or (Eeee(i, j) and i + j < 75))


for i in range(65):
    if h(7, i):
        print(i)
```

## Укороченные решатели

Частично укороченный решатель для 19 (выигрыш при наихудшем ходе Пети):
```python
from functools import lru_cache

@lru_cache(None)
def(a, b, c):
    if a + b + c >= 73: return 0
    ms = [
        (a + 3, b, c), (a, b + 3, c), (a, b, c + 3),
        (a + 13, b, c), (a, b + 13, c), (a, b, c + 13),
        (a + 23, b, c), (a, b + 23, c), (a, b, c + 23)
    ]
    if any(f(*turn) == 0 for turn in ms): return 1
    if any(f(*turn) == 1 for turn in ms): return 2

for s in range(1, 24):
    if f(2, s, 2*s) == 2:
        print(s)
        break
```

Частично укороченный решатель для заданий 20-21:

```python
from functools import lru_cache


@lru_cache(None)
def f(a, b):
    if a > b:
        turns = [(a, b + i) for i in range(1, b+1)]
    elif a < b:
        turns = [(a + i, b) for i in range(1, a+1)]
    else:
        turns1 = [(a, b + i) for i in range(1, b+1)]
        turns2 = [(a + i, b) for i in range(1, a+1)]
        turns = turns1 + turns2

    if a + b > 45:
        return 0
    if any(f(*turn) == 0 for turn in turns):
        return 1
    if all(f(*turn) == 1 for turn in turns):
        return 2
    if any(f(*turn) == 2 for turn in turns):
        return 3
    if all(f(*turn) in (1, 3) for turn in turns):
        return 4

for i in range(6, 41):
    if f(5, i) == 3:
        print("#"*4, i)
    if f(5, i) == 4:
        print("#"*8, i)
```

Некоторые пояснения по коду:

[[Разворачивание кортежа в вызове функции|Про `*turn`]].

TODO: вставить ссылки на другие объяснения.

Если интерпретатор ругается на превышение лимита глубины рекурсии, его можно увеличить, [[Импорт модулей|импортировав]] модуль sys:

```python
import sys
sys.setrecusionlimit(20000)
```

Решала-чемпион:

```python
def w(a, m):    # def w(a, b, m): — для двух куч
    if a >= 34: return m%2==0       # Условие победы
    if m == 0: return False         # Прекращаем перебор
    h = [w(a+2,m-1), w(a*3,m-1)]    # Перебор ходов
    return any(h) if m%2 else all(h)

print(19, [s for s in range(1, 34) if w(s, 2)])
print(20, [s for s in range(1, 34) if w(s, 3) and not w(s,1)])
print(21, [s for s in range(1, 34) if w(s, 4) and not w(s,2)])
```