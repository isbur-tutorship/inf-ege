with open('24_8431.txt') as f:
    isxod = f.read()

k = 0
maxk = 0
for troika in zip(isxod, isxod[1:], isxod[2:]):
    if set(troika) == {"X","Y","Z"}:
        maxk = max(maxk, k-2)
        k = 0
    else:
        k += 1
maxk = max(maxk, k) # чтобы учесть последний фрагмент

print(maxk)
