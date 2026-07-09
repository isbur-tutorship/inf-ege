# kompege-29348


from sys import *


setrecursionlimit(2000000)


def F(n):
    if n < 10:
        return 1
    else:
        return (n + 3) * F(n - 3)


print((F(247563)//519-477*F(247560))//F(247557))