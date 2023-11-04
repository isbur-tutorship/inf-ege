# ЕГЭ информатика 2024. Повторение

## Содержание
17. [Задание 17 (числовая последовательность)](#задание-17)

## Задание 17

### Чтение из файла

```python
f = open("17.txt")
A = f.readlines()
A = [int(x) for x in A]
```
Последняя строчка — более короткая запись для
```python
for i in range(len(A)):
    A[i] = int(A[i])
```
### Собственно решение задачи
#### Перебор пар (троек) последовательных значений
[Пример](https://inf-ege.sdamgia.ru/problem?id=59722)

> Элементы ряда могут принимать целые значения в диапазоне [−10000; 10000]. Определите количество троек элементов последовательности, в которой только одно число трехзначное, а сумма тройки меньше наибольшего числа, оканчивающегося на 17. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.

```python
f = open("17.txt")
A = f.readlines()
A = [int(x) for x in A]

max17 = -10000
for x in A:
    if abs(x) % 100 == 17 and x > max17:
        max17 = x

counter = 0
for i in range(len(A) - 2):
    # Пример техники работы с последовательными тройками
    B = []
    for j in range(3):
        B.append(A[i+j])
    C = []
    for j in range(3):
        C.append(len(str(abs(B[j]))))
    if C.count(3) == 1 and sum(B) < max17:
        counter += 1

print(counter)
```
#### Перебор всех возможных пар
Чтобы перебрать все пары различных элементов, можно использовать двойной вложенный цикл, например, так:
```python
max_s = 0
k = 0
for i in range(len(A)):
    for j in range(len(A)):
        s = A[i]+A[j]
        if s % 9 == 0:
            k += 1
            if s > max_s:
                max_s = s
```
Данная программа, при условии, что можно брать любые два элемента последовательности, а не только идущие друг за другом, считает количество пар элементов, сумма которых делится на 9 (переменная `k`), а также находит максимальную из таких сумм (переменная `max_s`).

## Задания 19—21
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

#m = 46
#m_i, m_j = 0, 0
#for i in range(1, 46):
#    for j in range(1, 46):
#        if f(i, j) == 1:
#            if (i + j) < m:
#                m = i + j
#                m_i = i
#                m_j = j
#
#print(m, m_i, m_j)

for i in range(6, 41):
    if f(5, i) == 3:
        print("#"*4, i)
    if f(5, i) == 4:
        print("#"*8, i)
```
