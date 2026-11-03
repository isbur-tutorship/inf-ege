def expr(x, A):
    return (x & A != 0) <= ((x & 10 == 0) <= (x & 3 != 0))
    
for A in range(1, 1000):
    if all(expr(x, A) for x in range(1, 1000)):
        print(A)