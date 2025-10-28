def f(N):
    N = bin(N)[2:]
    s = N.count("1")
    N += str(s % 2)
    s = N.count("1")
    N += str(s % 2)
    return int(N, 2)

for i in range(1, 100):
    if f(i) > 43:
        print(f(i))
        break