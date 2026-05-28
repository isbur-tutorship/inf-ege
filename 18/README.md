Решение номеров без стенок через Python:

```python
N = 10
f = open('18.csv')
A = [[int(x) for x in s.split(';')] for s in A]

B = [[0 for x in range(N)] for y in range(N)]
B[0][0] = A[0][0]
for i in range(1, N):
    B[i][0] = B[i-1][0] + A[i][0]
for j in range(1, N):
    B[0][j] = B[0][j-1] + A[0][j]
for i in range(1, N):
    for j in range(1, N):
        B[i][j] = min(B[i-1][j], B[i][j-1]) + A[i][j]

print(B[N-1][N-1])
```