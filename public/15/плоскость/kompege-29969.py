# kompege-29969

for A in range(1000):
    results = []
    for x in range(1000):
        for y in range(1000):
            results.append((x > A or y > A or x + 2*y < 80) == 1)
    if all(results):
        print(A)