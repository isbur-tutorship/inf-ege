for A in range(1, 1000):
    c = 0
    for x in range(1, 1001):
        if ((x & 47 == 0) or ( (x & 13 == 0) <= (not (x & A == 0)))) == 1:
            c += 1
    if c == 1000:
        print(A)
        break