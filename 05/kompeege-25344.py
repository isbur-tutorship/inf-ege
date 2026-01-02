Rs = []
for a in range(1, 100):
    R = ""
    s = 0
    while a != 0:
        R = str(a % 3) + R
        s = s + a % 3
        a = a // 3
    
    if int(R, 3) % 3 == 0:
        R = R + R[-2] + R[-1]
    else:
        R2 = ""
        s = s * 3
        while s != 0:
            R2 = str(s % 3) + R2
            s = s // 3
        R = R + R2
    
    R = int(R, 3)
    if R % 2 == 1 and R > 208:
        Rs.append(R)

print(min(Rs))