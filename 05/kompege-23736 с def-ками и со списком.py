def to3(n):
    s = ""
    while n != 0:
        s = str(n % 3) + s
        n = n // 3
    return s

A = []
for N in range(1,1000):
    R = to3(N)
    if N % 5 == 0:
        R = R + R[-2:]
    else:
        R = R + to3(N % 5 * 7)
    
    if int(R, 3) < 200:
        A.append(N)

print(sum(A) / len(A))