k = 0
for n in range(6_300_000, 10_000_000):
    A = []
    breakN = False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            A.extend([i, n // i])
            if len(A) > 6:
                breakN = True
                break
    if breakN == True:
        continue
    
    if len(A) != 6:
        continue
    
    maxI = 0
    has34 = True
    for i in A:
        isPrime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            if not("3" in str(i) or "4" in str(i)):
                has34 = False
                break
            maxI = max(i, maxI)
    
    if not has34:
        continue
    
    print(n, maxI)
    k += 1
        
    if k == 5:
        break