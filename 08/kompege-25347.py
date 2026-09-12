from itertools import product

d = "АГИНРТ"

# d = "ГРАНИТ"
# d = [x for x in d]
# d.sort()

c = 1
for n in product(d, repeat = 6):
    if (n[0] not in "АГИ") and n.count("А") == 1:
        print(n, c)
        break
    c += 1