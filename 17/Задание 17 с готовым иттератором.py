from itertools import pairwise

A = open("17-1.txt").readlines()
A = [int(x) for x in A]

# Если надо пофильтровать:
# maxA = max([x for x in A if x % 3 == 0])

B = [] 
for a, b in pairwise(A):
    if a % 3 == 0 or b % 3 == 0:
        B.append(a+b)
    
print(len(B), max(B))       