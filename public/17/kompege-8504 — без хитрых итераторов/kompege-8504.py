with open("17.txt") as f:
    asmr = [int(_) for _ in f.readlines()]
    
B = [_ for _ in asmr if (len(str(_)) == 3) and (str(_)[-1] == "5")]
min5 = min(B) # 125 — минимальный трёхзначный элемент последовательности, оканчивающийся на 5 (см. условие)

k = d = 0
for x in range(len(asmr) - 1):
    if (len(str(asmr[x])) == 3 or len(str(asmr[x + 1])) == 3) and (
        (asmr[x] + asmr[x + 1]) % min5 == 0):
        k += 1
        if asmr[x] + asmr[x + 1] > d:
            d = asmr[x] + asmr[x + 1]

print(k, d)
