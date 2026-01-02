for A in range(1, 100):
    s = ""
    for x in range(-100, 100):
        # ¬ДЕЛ(x, А) → (ДЕЛ(x, 6) → ¬ДЕЛ(x, 9))
        e = (not (x % A == 0)) <= ((x % 6 == 0) <= (not (x % 9 == 0)))
        if e:
            s += "#"
        else:
            s += "_"

    if s.count("_") == 0:
        print(s)
        print(A)
        # exit()