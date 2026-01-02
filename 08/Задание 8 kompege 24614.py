from itertools import *

A = set()
k = 0
for c in set(permutations("КОНФЕТЫ ИЛИ ЖИЗНЬ", 7)):
    s = "".join(p)
    if "  " in s:
        k += 1

print(k)