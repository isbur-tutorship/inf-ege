for A in range(0, 100):
    d = ""
    for x in range(15):
        s = ""
        for y in range(15):
            # ( (yy  A) → (y  10) )  ( (x  9) → (xx < A) )
            e = ((y**2 <= A) <= (y <= 10)) and ((x <= 9) <= (x**2 < A))
            if e:
                s += "#"
            else:
                s += "_"
        s += "\n"
        d += s
    if d.count("_") == 0:
        print(d)
        print(A)
        break