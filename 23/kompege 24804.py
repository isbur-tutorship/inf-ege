def f(a, b, c):
    if a > b: return 0
    if a == b: return 1
    if a == 4: c = True
    if a == 16 and c == True: return 0
    return f(a*2,b,c) + f(a**2,b,c) + f(a**3,b,c)

print(f(2, 131072, False))