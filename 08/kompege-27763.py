# kompege-27763

from itertools import *

c = 0
for w in product("0123456", repeat = 5):
    if w[0] == "0":
        continue
        
    if w.count("0") == 1 and w.count("1") <= 2:
        c += 1
        
print(c)