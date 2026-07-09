A = [int(x) for x in open("17-var-25194722.txt")]

min17 = min(x for x in A if 999 < abs(x) < 10000 and x % 17 == 0)

k = 0
minsum = 3*10**4+1
for a, b, c in zip(A, A[1:], A[2:]):
    # Компактное условие:
    # if any(999 < abs(x) < 10000 and abs(x) % 100 == 27 for x in a,b,c):
    # Без any:
    if 999 < abs(a) < 10000 and abs(a) % 100 == 27 or 999 < abs(b) < 10000 and abs(b) % 100 == 27 or 999 < abs(c) < 10000 and abs(c) % 100 == 27:
        if a**2 + b**2 + c**2 <= min17**2:
            k += 1
            minsum = min(abs(a) + abs(b) + abs(c), minsum)

print(k, minsum)
