programs = [""]

for _ in range(4):
    new_programs = []

    for p in programs:
        new_programs.append(p + "a")
        new_programs.append(p + "b")

    programs = new_programs