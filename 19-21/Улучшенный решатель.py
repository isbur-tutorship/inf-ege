def w(a, m):
    if a > 83: return m%2==1
    if 34 <= a <= 83: return m%2==0
    if m == 0: return False
    h = [w(a+2,m-1), w(a*3,m-1)]
    return any(h) if m%2 else all(h)

print(19, [s for s in range(1, 34) if w(s, 1)])
print(20, [s for s in range(1, 34) if w(s, 3) and not w(s,1)])
print(21, [s for s in range(1, 34) if w(s, 4) and not w(s,2)])