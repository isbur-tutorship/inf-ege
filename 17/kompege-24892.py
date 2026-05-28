f = open('17_24892.txt')
a = [int(x) for x in f]
k = 0

maxa = max([x for x in a if 999<abs(x)<10000 and x % 9 == 0])

for i in range(len(a)-1):
    if a[i] < 0 and a[i+1]> maxa:
        k += 1

print(k)    
