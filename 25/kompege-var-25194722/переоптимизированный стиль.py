k = 0
for n in range(6_300_000, 10_000_000):
    x = n
    A = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            A.append(d)
            n //= d
        if len(A) > 2:
            break
        d += 1
    if n > 1:
        A.append(n)
    if len(A) != 3:
        continue
    
    maxI = max(A)

    has34 = True
    for i in A:
        if not("3" in str(i) or "4" in str(i)):
            has34 = False
            break    
    
    if has34:
        print(x, maxI)
        k += 1
        
    if k == 5:
        break
