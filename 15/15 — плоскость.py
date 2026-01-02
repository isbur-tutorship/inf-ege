def expr(x, y, A):
    return (y + 2*x < A) or ( x > 20 ) or ( y > 40 )
    
for A in range(-200, 200):
    red_flag = False
    for x in range(-200,200):
        for y in range(-200,200):
            if expr(x, y, A) == False:
                red_flag = True
                break
        if red_flag:
            break
    if red_flag == False:
        print(A)