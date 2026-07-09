# kompege-29968

for x in range(1, 3001):
    n = 9*11**210 + 8*11**150 - x
    c = 0
    while n > 0:
        if n % 11 == 0:
            c += 1
        n //= 11
    if c == 60:
        print(x)