from itertools import product

print("a b c d")
for a,b,c,d in product([0,1], repeat = 4):
    if d and ((a or not c) <= (a and b and not c)):
        print(a,b,c,d)