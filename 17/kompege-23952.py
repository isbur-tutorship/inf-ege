f = open('17_23952.txt')
h = [int(i) for i in f]
k = 0

maxa = max([x for x in h if x % 100 == 93])

hf = []
for i in h:
    if i % 100 == 93:
        hf.append(i)
maxa = max(hf)

for i in range(len(h)-1):
    if (h[i]>maxa and h[i+1] <= maxa or h[i]<=maxa and h[i+1]>maxa) and (str(h[i])[0]=="9" or str(h[i+1])[0] == "9"):
        k += 1

print(k)
