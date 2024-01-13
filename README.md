# ЕГЭ информатика 2024. Повторение

## Содержание
2.  [Задание 2 (анализ логического выражения)](#задание-2)
13. [Задание 13 (IP-адреса и маски подсетей)](#задание-13)
17. [Задание 17 (числовая последовательность)](#задание-17)
19. [Задания 19—21 (теория игр)](#задания-1921)
25. [Задание 25 (перебор чисел)](#задание-25)
26. [Задание 26 (что-то с сортировкой)](#задание-26)
### Архив
13. [Задание 13 (подсчёт числа путей в графе)](#задание-13-old)


## Задание 2
Пример задания:
> Логическая функция F задаётся логическим выражением y &and; (x &or; z) &or; &not;(y &or; z) &or; w. На рисунке приведён частично заполненный фрагмент таблицы исинности функции F, содержащий неповторяющиеся строки. Определите, какому столбцу таблицы истинности соответствует каждая из пременных w, x, y, z.

|?|?|?|?|F|
|-|-|-|-|-|
|1| |0|1|0|
| |1|0| |0|
|0|0| |1|0|

> В ответе напишите буквы w, x, y, z в том порядке, в котором идут соответствующие им столбцы. Буквы в ответе пишите подряд, никаких разделителей между буквами ставить не нужно.

Напишем программу на Python ([Е. Барджахаров](https://t.me/televoliks)):
```python
# y ∧ (x ∨ z) ∨ ¬(y ∨ z) ∨ w
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (y and (x or z) or (not (y or z)) or w) == 0:
                    print(x, y, z, w)
```
Она выдаёт следующую таблицу:
|x|y|z|w|
|-|-|-|-|
|0|0|1|0|
|0|1|0|0|
|1|0|1|0|

Её можно вырезать при помощи клавиши PrtSc или инструмента "Ножницы" и вставить в Paint, а дальше заняться следующим: по мере открытия новой информации о задаче выделяем целый столбец или строку, меняем их местами с другими столбцами/строками, так получается красиво и наглядно.

Обратим внимание, что в исходной таблице единицы есть во всех столбцах, кроме третьего, а в полученной из программы таблицы есть столбец, состоящий из одних только нулей. Значит, столбец w — третий, поменяем третий и четвёртый столбцы местами:
|x|y|w|z|
|-|-|-|-|
|0|0|0|1|
|0|1|0|0|
|1|0|0|1|

Поменяем местами первую и третью строчки, просто "патамушта" (tip: так мы добьёмся идеального совпадения с исходной таблицей):
|x|y|w|z|
|-|-|-|-|
|1|0|0|1|
|0|1|0|0|
|0|0|0|1|

О, значит,

**Ответ:** xywz.
### Совет
Педантично расставляем скобки при использовании `<=` вместо импликации, ибо может получиться "что-то не то":
```python
> 3 % 3 == 0 <= False
True
> (3 % 3 == 0) <= False
False
```


## Задание 13

Есть удобная функция в Excel для перевода десятичных чисел в двоичные: `ОСНОВАНИЕ(<КОНВЕРТИРУЕМОЕ ЧИСЛО>; <ОСНОВАНИЕ ЦЕЛЕВОЙ СИСТЕМЫ СЧИСЛЕНИЯ>; <РАЗРЯДНОСТЬ ЧИСЛА>)`.

Это практичнее, чем использовать встроенную функцию `bin()` в Python: проще не забыть про ведущие нули.


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

### Small tip
Остаток от деления отрицательного числа — это _дополнение_ этого числа до делителя, например:
```python
>>> -117 % 100
83
```
Поэтому чтобы не получать неожиданных результатов от операций взятия остатка, надо брать остаток от модуля (`abs(n)`) от этого числа.

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

## Задание 25
### Перебор с маской
[Пример](https://inf-ege.sdamgia.ru/problem?id=60267)
> Среди натуральных чисел, не превышающих 10^10, найдите все числа, соответствующие маске 1?2157*4, делящиеся на 2024 без остатка. В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце  — соответствующие им результаты деления этих чисел на 2024.
```python
from fnmatch import fnmatch

for n in range(0, 10**10, 2024):
    if fnmatch(str(n), "1?2157*4"):
        print(n, n // 2024)
```

## Задание 26
### Сюжет: администратор и файлы
Пример — задача 225 с kompege.ru
```python
with open("26.txt") as f:
    S, N = [int(_) for _ in f.readline().split()]
    A = [int(_) for _ in f.readlines()]

A.sort(reverse=True)

print(A[:100])

s = 0
i = 0
while s + A[i] < S:
    s += A[i]
    i += 1

for j in range(i, len(A)):
    if A[j] <= S - s:
        s += A[j]
        break
    
print(i + 1, A[j])
```

## Архив

## Задание 13 (old)
Возможно решение через Python!
Можно задать граф в одну строчку, записать это всё в словарь, а затем итерироваться по словарю, чтобы подсчитать число вершин. Если нужно что-то исключить, то модифицируем граф.
