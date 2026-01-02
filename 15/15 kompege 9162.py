for A in range(-13, 100):
    flag = True
    for x in range(1, 100):
        for y in range(1, 100):
            expr = (not(x*y > A+13)) <= ((28*y > 520) or (25*x > 800))
            if expr != True:
                flag = False
    if flag:
        print(A)