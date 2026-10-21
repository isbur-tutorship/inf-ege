# kompege-29953
from itertools import permutations
# Чтобы быстрее писать:
# from itertools import *

def F(x,y,w,z):
    # ¬((x→w)→(w≡z))∧y
    return not ((x <= w) <= (w == z)) and y
 
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    t = (
                        (a, 0, 1, 0),
                        (0, b, c, 0),
                        (d, 1, 1, e)
                    )
                    
                    if len(set(t)) < 3: # Сколько неповторяющихся строк в таблице
                        continue
                    
                    for p in permutations('xywz'):
                        if all(F(**dict(zip(p, row))) for row in t):
                            print(p)
                    
                    