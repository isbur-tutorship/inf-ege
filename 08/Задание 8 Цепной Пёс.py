from itertools import product

c = 0
for word in product("ABCX", repeat = 5):
    print(word[:4], word)
    if 'X' not in word[0:4]:
        c += 1

print(c)