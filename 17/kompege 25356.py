A = [int(x) for x in open("17_25356.txt")]
max30 = max([x for x in A if x % 100 == 30])
count = 0
maxsum = -10**10
for i in range(len(A) - 2):
    a, b, c = A[i], A[i+1], A[i+2]
    # if all(len(str(abs(A[i]))) != 4 for i in (i, i+1, i+2)) and a+b+c > max30:
    # if all(not (1000 <= abs(A[j]) <= 9999) for j in range(i, i+3)) and a+b+c > max30:
    if not 1000 <= abs(a) <= 9999 and not 1000 <= abs(b) <= 9999 and not 1000 <= abs(c) <= 9999 and a+b+c > max30:
        count += 1
        maxsum = max(maxsum, a+b+c)
  
print(count, maxsum) 

print(max([a+b+c for a,b,c in zip(A,A[1:],A[2:]) if all([not(1000 <= abs(x) <= 9999) for x in (a,b,c)]) and a+b+c > max30]))
print(len([a+b+c for a,b,c in zip(A,A[1:],A[2:]) if all([not(1000 <= abs(x) <= 9999) for x in (a,b,c)]) and a+b+c > max30]))