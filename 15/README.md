## Отрезки

### Решение через "подсказку":

#### Пример
> На числовой прямой даны два отрезка: P = [5, 30] и Q = [14, 23]. Укажите наибольшую возможную длину промежутка A, для которого формула
>
>((x ∈ P) ≡ (x ∈ Q)) → ¬(x ∈ A)
>
> тождественно истинна, то есть принимает значение 1 при любом значении переменной _х_.

```python
s = ""
P = range(5, 31)
Q = range(14, 24)
# A = []
# либо можно пробовать A = range(5, 31) (то есть накрывающий всю область задачи), если получается бессмыслица
# Даже так: если спрашивают наибольшую длину отрезка, то надо брать A, покрывающее всю область задачи
# Если же спрашивают про наименьшую длину, то брать A равно пустому списку
A = range(5, 14)
#A = range(25, 31)
for x in range(5, 40):
        expr = ((x in P) == (x in Q)) <= (not (x in A))
        s += str(int(expr))
print(s)
```

### Решение через "подсказку" и рациональные числа:

```python
def P(x): return 2 <= x <= 20
def Q(x): return 15 <= x <= 25

A = []
counter = 0
for i in range(80*5):
    x = 0.2*i
    expr = ((not (x in A)) <= (not P(x) or Q(x)))
    if expr == 0:
        counter += 0.2
    print(int(expr), end = "")
        
print(counter)
```
## Поразрядная конъюнкция

![[Pasted image 20260524145519.png]]

Подход с all():
```python
for A in range(1, 1000):
	if all( (x & 47 == 0) or ( (x & 13 == 0) <= (not (x & A == 0)) == 1 for x in range(1, 1000) ) ):
		print(A)
		break
```
Подход со счётчиком:
```python
for A in range(1, 1000):
    c = 0
    for x in range(1, 1001):
        if ((x & 47 == 0) or ( (x & 13 == 0) <= (not (x & A == 0)))) == 1:
            c += 1
    if c == 1000:
        print(A)
        break
```

## Плоскость

```python
for A in range(100):
    results = []
    for y in range(100):
        for x in range(100):
            expr = (y + 2*x < A) or (x > 20) or (y > 30)
            results.append(expr)
    if all(results):
        print(A)
        break
```

## Общие советы

### Педантично расставляйте скобки!


```python
print(False <= False)     # True
print(False <= True)      # True
print(True <= False)      # False
print(True <= True)       # True

print(False == 0)
print(True == 1)

print(3 % 3 == 0 <= False)
print((3 % 3 == 0) <= False)
```

