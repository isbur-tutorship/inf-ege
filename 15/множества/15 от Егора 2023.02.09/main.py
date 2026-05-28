A = []
B = [2, 4, 6, 8, 10, 12]
C = [4, 8, 12, 116]

s = ""
for x in range(1, 151):
    expr = (x in B) <= (((x in C) and (not(x in A))) <= (not(x in B)))
    s += str(int(expr))
print(s)
print(s.count('0'))
