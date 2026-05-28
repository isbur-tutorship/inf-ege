f = [x for x in open('24_28765.txt')][0]#.replace("\n", "")
f = f.split("BC")
maxn = 0
for i in range(len(f) - 181):
    a = f[i:i+181]
    maxn = max(len("BC".join(a)), maxn)
print(maxn + 2)
