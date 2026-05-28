A = [int(x) for x in open("17_27629.txt")]
max43 = max([x for x in A if x % 100 == 43 and 1000 <= x <= 9999])
count = 0
maxsum = -10**10
for i in range(len(A) - 1):
    a, b = A[i], A[i+1]
    if (1000 <= abs(a) <= 9999 or 1000 <= abs(b) <= 9999) and (a+b)**2 < max43**2 and (1000<= max43 <= 9999):
        count += 1
        maxsum = max(maxsum, (a+b)**2)
  
print(count, maxsum)
