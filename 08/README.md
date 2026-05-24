# Задание 8

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

Решение с применением библиотеки `itertools`:

```python
from itertools import product

counter = 0
for n in product("1234", repeat=5):       
    counter += n.count("1") == 2
    
print(counter)
```

Хорош, когда все слова одной фиксированной длины (подавляющее большинство задач).

Этот и другие представители модуля `itertools`:

```python
for a in product("ABC", repeat=3): print(a)
```
![[Pasted image 20260525010553.png]]
![[Pasted image 20260525010634.png]]
![[Pasted image 20260525010653.png]]

## Комбинаторное решение

Перестановки с повторениями:
https://www.matburo.ru/tvart_sub.php?p=calc_PR
Количество перестановок всех объектов делим на количества перестановок внутри групп этих объектов.

## Рекурсивный перебор

Может понадобиться в ситуации, когда длина слов переменная.

### Пример

> Ксения составляет слова из букв К, С, Е, Н, И, Я. Каждая гласная буква встречается в слове не более двух раз. Каждая согласная может стоять в слове на первой позиции, либо не встречаться вовсе. Сколько слов длиною более двух символов может составить Ксения?

Брутфорс с длиной слов переменной длины:

```python

global A

def f(a, n):
    if n >= 1:
        for x in "ЕИЯ":
            f(a+x, n-1)
    else:
        if all(a.count(_) <= 2 for _ in "ЕИЯ") and len(a.replace(".", "")) > 2:
            A.add(a)

A = set()
for l in ".КСН":
    for i in range(1, 8):
        f(l, i)

print(len(A))
```

Чуть более изящный (в алгоритмическом плане) вариант:

```python
global A

def f(s, a, n):
    if n >= 1:
        for i, x in enumerate(s):
            f(s[:i] + s[i+1:], a+x, n-1)
    else:
        if len(a.replace(".", "")) > 2:
            A.add(a)

A = set()
for l in ".КСН":
    for e in range(3):
        for i in range(3):
            for ya in range(3):
                s = "Е"*e + "И"*i + "Я"*ya
                f(s, l, len(s))

print(len(A))
```

Как памятник человеческой глупости:

```python
global A

def f(s, a, n):
    if n >= 1:
        for x in s:
            f(s, a+x, n-1)
    else:
        if all([a.count("Е") <= 2, a.count("И") <= 2, a.count("Я") <= 2]) and len(a.replace(".", "")) > 2:

            A.add(a)

A = set()
for l in ".КСН":
    for e in range(3):
        for i in range(3):
            for ya in range(3):
                s = "Е"*e + "И"*i + "Я"*ya
                f(s, l, len(s))

print(len(A))
```