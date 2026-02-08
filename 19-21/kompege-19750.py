def f(a, b):

    if 0 <= a <= 19: return b%2==0
    if b == 0: return False

    h = [f(a-5, b-1)]
    if a % 2 == 0:
        h.append(f(a // 2, b-1))
    if a % 3 == 0:
        h.append(f(a // 3, b-1))
    if a % 2 != 0 and a % 3 != 0:
        h.append(f(a+1,b-1))

    return any(h) if b%2 else all(h)


print(19, [s for s in range(100, 19, -1) if f(s, 2)])
print(20, [s for s in range(19, 100) if f(s, 3) and not f(s, 1)])
print(21, [s for s in range(19, 100) if f(s, 4) and not f(s, 2)])