for a in range(-100, 100):
    for b in range(a, 100):
        s = ""
        for x in range(-15, 15):
            # ( (x  A) → (x2  81) )  ( (x2  64) → (x  A) )
            # ( (x ⋲ A) → (x2 ≤ 144) ) ∧ ( (x2 – 10x ≤ 11) → (x ⋲ A) )
            x_in_A = a <= x <= b
            e = ( ( x_in_A ) <= (x**2 <= 144)) and (( x**2 - 10*x <= 11) <= ( x_in_A ))
            if e:
                s += "#"
            else:
                s += "_"

        if s.count("_") == 0:
            print(s)
            print(a, b)
            # exit()