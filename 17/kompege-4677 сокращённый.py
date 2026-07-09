# kompege-4677

A = [int(x) for x in open("17_4677.txt")]

k = len([x for x in A if x % 100 == 0])

B = [a + b for a, b in zip(A, A[1:]) if (a < 0 or b < 0) and a + b < k]

print(abs(max(B)), len(B))