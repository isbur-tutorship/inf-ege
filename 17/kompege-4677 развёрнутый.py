# kompege-4677

A = [int(x) for x in open("17_4677.txt")]

k = len([x for x in A if x % 100 == 0])

c = 0
maxsum = -10**7
for i in range(len(A) - 1):
    a = A[i]
    b = A[i+1]
    if (a < 0 or b < 0) and a + b < k:
        c += 1
        maxsum = max(maxsum, a + b)
        
print(abs(maxsum), c)