### Сюжет: администратор и файлы (почти не актуально в 2026)
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
