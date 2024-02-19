# ЕГЭ информатика 2024. Повторение

## Содержание
2.  [Задание 2 (анализ логического выражения)](#задание-2)
8.  [Задание 8 (комбинаторика)](#задание-8)
13. [Задание 13 (IP-адреса и маски подсетей)](#задание-13)
14. [Задание 14 (работа с разными системами счисления)](#задание-14)
17. [Задание 17 (числовая последовательность)](#задание-17)
19. [Задания 19—21 (теория игр)](#задания-1921)
20. [Задания 19—21 (теория игр)](#задания-1921)
21. [Задания 19—21 (теория игр)](#задания-1921)
23. [Задание 23 (рекурсия)](#задание-23) 
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


## Задание 8

Задание:
> Шифр кодового замка представляет собой последовательность из пяти символов, каждый из которых является цифрой от 1 до 4. Сколько различных вариантов шифра можно задать, если известно, что цифра 1 встречается ровно два раза, а каждая из других допустимых цифр может встречаться в шифре любое количество раз или не встречаться совсем?

```python
цифры = "1234"

counter = 0
for a in цифры:
    for b in цифры:
        for c in цифры:
            for d in цифры:
                for e in цифры:
                    n = a + b + c + d + e
                    if n.count("1") == 2:
                        counter += 1
print(counter)
```

Перестановки с повторениями:
https://www.matburo.ru/tvart_sub.php?p=calc_PR
Количество перестановок всех объектов делим на количества перестановок внутри групп этих объектов.


## Задание 13

Есть удобная функция в Excel для перевода десятичных чисел в двоичные: `ОСНОВАНИЕ(<КОНВЕРТИРУЕМОЕ ЧИСЛО>; <ОСНОВАНИЕ ЦЕЛЕВОЙ СИСТЕМЫ СЧИСЛЕНИЯ>; <РАЗРЯДНОСТЬ ЧИСЛА>)`. Соответственно, можно сделать такую таблицу:
||Первый байт|Второй байт|Третий байт|Четвёртый байт|Первый байт|Второй байт|Третий байт|Четвёртый байт|
|-|-|-|-|-|-|-|-|-|
|Адрес узла|192|168| 1 | 1 |=ОСНОВАНИЕ(A2;2;8)|=ОСНОВАНИЕ(B2;2;8)|=ОСНОВАНИЕ(C2;2;8)|=ОСНОВАНИЕ(D2;2;8)|
|Маска сети|255|255|255|248|=ОСНОВАНИЕ(A3;2;8)|=ОСНОВАНИЕ(B3;2;8)|=ОСНОВАНИЕ(C3;2;8)|=ОСНОВАНИЕ(D3;2;8)|

И, соответственно, глазками анализировать IP-адрес, применять побитовую конъюнкцию и прочее, прочее.

Это нагляднее, чем использовать встроенную функцию `bin()` в Python: проще не забыть про ведущие нули.

Впрочем, Питону есть чем ответить: функция `format(<ЧИСЛО>, "08b")` делает то же самое.

А ещё в Питоне в стандартной библиотеке есть пакет ipaddress, который может существенно помочь, если создатели задания упорются и решат, что делать этот номер решаемым вручную - не комильфо, и надо будет решать всё тупым перебором.

Чтобы импортировать модуль:
```python
from ipaddress import ip_network
```
### Претификаторы 
(команды для форматированного вывода IP-адресов, полезно использовать во время обучения, бесполезны на экзамене):
```python
'{:_b}'.format(my_ip_address)
```

Быстр в написании, если запомнить магическую комбинацию символов в начале, можно использовать на экзамене. Разбивает IP-адрес в двоичном представлении на тетрады:
```python
nw = ip_network('192.168.1.0/32')
print('{:_b}'.format(nw.network_address))
```
Вывод:
```
1100_0000_1010_1000_0000_0001_0000_0000
```

Красивый и сложный:
```python
def mf(addr):
    return " ".join([format(int(byte), "08b") for byte in str(addr).split(".")])
```

Представляет IP-адрес в виде 4 байтов, представленных в виде двоичного кода, разделённых пробелами:
```python
nw = ip_network('192.168.1.0/32')
print(mf(nw.network_address))
```
Вывод:
```
11000000 10101000 00000001 00000000
```

### Примеры использования пакета ipaddress

\*Догадайтесь сами, что всё это значит\*

```python
nw = ip_network('157.180.63.114/255.255.255.248', False)
addr = nw.network_address
print(mf(addr))
print(mf(nw.broadcast_address))
print(mf(nw.hostmask))
print(mf(nw.netmask))
print(nw.num_addresses)
for addr in nw.hosts():
    print(addr)
```

### Примеры решения задач
> В терминологии сетей TCP/IP маской сети называется двоичное число, определяющее, какая
> часть IP-адреса узла сети относится к адресу сети, а какая — к адресу самого узла в этой сети.
> Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу
> узла и маске сети.
> Сеть задана IP-адресом 157.180.63.114 и маской сети 255.255.255.248. Сколько в этой сети IP-
> адресов, для которых в двоичной записи IP-адреса суммарное количество единиц в левых двух
> байтах меньше суммарного количества единиц в правых двух байтах? В ответе укажите только
> число.

```python
nw = ip_network('157.180.63.114/255.255.255.248', False)
counter = 0
for i in range(0, nw.num_addresses):
    addr = nw.network_address + i
    addr = bin(int(addr))[2:].zfill(32)
    left = addr[:16]
    right = addr[16:]
    if left.count("1") < right.count("1"):
        counter += 1
print(counter)
```

> В терминологии сетей TCP/IP маской сети называется двоичное число, определяющее, какая
> часть IP-адреса узла сети относится к адресу сети, а какая — к адресу самого узла в этой сети.
> Адрес сети получается в результате применения поразрядной конъюнкции к заданному адресу
> узла и маске сети.
> Сеть задана IP-адресом 255.112.128.136 и маской сети 255.255.Х.0, где Х - число, заданное в
> диапазоне от 0 до 255. Определите минимальное значение Х, для которого для всех IP-адресов
> этой сети в двоичной записи IP-адреса суммарное количество единиц в левых двух байтах не
> менее суммарного количества единиц в правых двух байтах. В ответе укажите только число.

```python
def chuck(nw):
    counter = 0
    for i in range(0, nw.num_addresses):
        addr = nw.network_address + i
        #print(mf(addr))
        addr = bin(int(addr))[2:].zfill(32)
        #print(addr)
        left = addr[:16]
        right = addr[16:]
        if left.count("1") >= right.count("1"):
            counter += 1
    return counter == nw.num_addresses

for i in range(0, 256):
    try:
        nw = ip_network(f'255.112.128.136/255.255.{i}.0', False)
    except:
        continue
    else:
        print(nw.network_address)
        if chuck(nw):
            print(i)
            print(chuck(nw))
            break
```


## Задание 14

| Перевод... | Функция |
|-|-|
| ...из десятичной в двоичную          | `bin(x)` |
| ...из десятичной в восьмеричную      | `oct(x)` |
| ...из десятичной в шестнадцатиричную | `hex(x)` |

Примеры самописных функций перевода:
```python
# 10 -> 13

def encode(x):
    digits = "0123456789abc"
    return digits[x]

def f(x):
    if x < 13:
        return encode(x)
    else:
        return f(x // 13) + encode(x % 13)

print(f(2024))

# 10 -> 6

def g(x):
    if x < 6:
        return str(x)
    else:
        return g(x // 6) + str(x % 6)

print(g(2024))

# 10 -> 7

def h(x):
    s = ""
    while x > 0:
        s = str(x % 7) + s
        x //= 7
    return s

print(h(2024))
```


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

> * Задание 1 из домашней работы Флеша *

Можно делать через Excel:

https://docs.google.com/spreadsheets/d/1iB98T5RNAmyIp3He0m0ZHyAwhQTXvJqJ9lKNiY--d8I/edit#gid=525142007

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

Краткое рекурсивное решение для заданий 20-21:

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

## Задание 23
Пример:
> # Задание 20
>
>Исполнитель преобразует число на экране.
>У исполнителя есть четыре команды, которым присвоены номера:
>1. Прибавить 1
>2. Прибавить 2
>3. Умножить на 2
>4. Умножить на 3
>Первая команда увеличивает число на экране на 1, вторая увеличивает его на 2, третья умножает на
>2, четвёртая — умножает на 3.
>Программа для исполнителя — это последовательность команд. Например, если в начальный
>момент на экране находится число 1, то программа 213 последовательно преобразует его в 3, 4, 8.
>Сколько существует программ, которые преобразуют исходное число 1 в число 24 и при этом не
>содержат двух последовательных команд сложения и двух последовательных команд умножения?

Программа:
```python
from functools import lru_cache


@lru_cache(maxsize=None)
def f(x, n, s):
    # print(n)
    if x > n:
        return 0
    elif x == n:
        return 1
    elif s == 1 or s == 2:
        return f(x * 2, n, 3) + f(x * 3, n, 4)
    elif s == 3 or s == 4:
        return f(x + 1, n, 1) + f(x + 2, n, 2)
    else:
        return f(x+1, n, 1) + f(x * 3, n, 4) + f(x * 2, n, 3) + f(x+2, n, 2)


print(f(1, 24, 0))
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
