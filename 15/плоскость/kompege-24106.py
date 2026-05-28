for A in range(1, 1000):
    c = 0
    for x in range(1, 100+1):
        for y in range(1, 100+1):
            if (2*x*y>A or y < x or x < 15) == 1:
                c = c + 1
    if c == 100**2:
        print(A)