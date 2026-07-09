# kompege-28696

from itertools import *

odd = "13579bd"

c = 0
for w in product("0123456789abcd", repeat = 5):
    
    if w[0] == "0":
        continue
    
    if len([l for l in w if l in odd]) != 2:
        continue
    
    for i in range(len(w) - 2):
        a = w[i]
        b = w[i + 2]
        if a == b and a in odd:
            c += 1

print(c)
