f = [int(x) for x in open("17_28762.txt")]

g = [x for x in f if x % 23 == 0]
ming = min(g)

c = 0
maxsum = 0
for i in range(len(f) - 1):
    a = f[i]
    b = f[i+1]
    if a % ming == 0 or b % ming == 0:
        c = c + 1
        maxsum = max(maxsum, a + b)

print(c, maxsum)