# kompege-var-25194722

def w(a, b, m):
    if a*b >= 541: return m%2==0
    if m == 0: return False
    h = [w(a+10,b,m-1), w(a*2,b,m-1),w(a,b+10,m-1), w(a,b*2,m-1)]
    return any(h) if m%2 else all(h)

print(19, [s for s in range(1, 91) if w(6, s, 2)])
print(20, [s for s in range(1, 91) if w(6, s, 3) and not w(6, s,1)])
print(21, [s for s in range(1, 91) if w(6, s, 4) and not w(6, s,2)])