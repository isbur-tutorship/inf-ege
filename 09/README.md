https://stepik.org/course/100056/syllabus — неплохой блок упражнений на Excel

Можно сохранить в Excel как .CSV файл, открыть в Python как обычный текстовый файл и решать задачу через программу!

```python
f = open('9.csv')
A = [[int(x) for x in s.split(';')] for s in f]
counter = 0
for triplet in A:
    a = min(triplet)
    b = max(triplet)
    c = sum(triplet) - a - b
    if c == (a + b) / 2:
        counter += 1

print(counter)
```