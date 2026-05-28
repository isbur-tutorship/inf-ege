def f(q,w="hui"):
    s = q % 10 + q // 10 % 10
    if q == w:
        return 1
    if q < w:
        return 0
    return f(q-4,w)+f(q-s,w)
        
print(f(36,14)*f(14,2))