# kompege-28694

from itertools import *

even = "02468a"

c = 0
for w in product("0123456789ab", repeat = 5):
    if w[0] == "0":
        continue
    
    s = 0
    for l in w:
        if l in even:
            s += 1
    
    if s != 2:
        continue

    for i in range(len(w) - 1):
        a = w[i]
        b = w[i+1]
        if a in even and a == b:
            c += 1
                    
print(c)