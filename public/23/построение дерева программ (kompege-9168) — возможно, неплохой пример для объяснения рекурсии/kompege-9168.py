programs = []

for a in "ab":
    for b in "ab":
        for c in "ab":
            for d in "ab":
                programs.append(a + b + c + d)

results = []

for program in programs:
    x = 1

    for command in program:
        if command == "a":
            x += 2
        else:
            x *= 3

    results.append(x)

print(len(set(results)))