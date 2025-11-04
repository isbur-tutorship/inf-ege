def g(a, b, c, m):
    if a + b >= 55: return c%2 == m%2
    if c == m: return 0
    t = [(a+1, b),(a,b+1),(a*2,b),(a,b*2)]
    h = [g(*_, c+1, m) for _ in t]
    return any(h) if (c+1)%2 == m%2 else all(h)

for s in range(1, 50):
    for m in range(1, 6):
        if g(5, s, 0, m):
            print(s, m)
            break