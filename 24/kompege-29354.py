#kompege-29354

f = open("24_29354.txt")
s = f.read()
s = s.split("BC")
maxn = 0
for i in range(len(s) - 191):
    n = len("C" + "BC".join(s[i:i+191]) + "B")
    maxn = max(maxn, n)
    
print(maxn)