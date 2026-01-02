from sys import *

setrecursionlimit(100000)

def F(n):
    if n >= 19:
        return F(n-4) + 3580
    else:
        return 6*(G(n-7) - 36)

def G(n):
    if n >= 248045:
        return n/20 + 28
    else:
        return G(n+9) - 4

print(F(673))