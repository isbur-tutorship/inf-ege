P = range(25, 31)
Q = range(15, 21)
# A = []
A = range(0, 41)
# ( (x  А) → (x  P) ) \/ (x  Q)
for x in range(0,41):
    expr = ((x in A) <= (x in P)) or (x in Q)
    if expr:
        print("#", end = "")
    else:
        print("_", end = "")
    if x % 5 == 0:
        print("|", end = "")