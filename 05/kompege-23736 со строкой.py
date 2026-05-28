for N in range(1, 1000):
    R = N
    s = ""
    while R != 0:
        s = str(R % 3) + s
        R //= 3
    if N % 5 == 0:
        s = s + s[-2] + s[-1]
    else:
        dovesok = (N % 5) * 7
        t = ""
        while dovesok != 0:
            t = str(dovesok % 3) + t
            dovesok //= 3
        s = s + t
    R = int(s, 3)
    if R <= 273:
        print(N)