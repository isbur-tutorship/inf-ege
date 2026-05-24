from itertools import product

c = 1
for _67_ in product(sorted("БУРАТИНО"), repeat = 5):
    if _67_[0] not in "УАИО" and _67_.count("Б") <= 1 and _67_.count("У") <= 1 and _67_.count("Р") <= 1 and _67_.count("А") <= 1 and _67_.count("Т") <= 1 and _67_.count("И") <= 1 and _67_.count("Н") <= 1 and _67_.count("О") <= 1:
        print(c)
    c += 1