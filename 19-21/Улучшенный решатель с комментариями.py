def w(a, m):    # def w(a, b, m): — для двух куч
    if a >= 34: return m%2==0       # Условие победы
    if m == 0: return False         # Прекращаем перебор
    h = [w(a+2,m-1), w(a*3,m-1)]    # Перебор ходов
    return any(h) if m%2 else all(h)

print(19, [s for s in range(1, 34) if w(s, 1)])
print(20, [s for s in range(1, 34) if w(s, 3) and not w(s,1)])
print(21, [s for s in range(1, 34) if w(s, 4) or w(s,2)])