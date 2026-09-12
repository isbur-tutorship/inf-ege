A = [0, 1]
for w in A:
    for x in A:
        for y in A:
            for z in A:
                # x ∧ (¬z ∨ w) ∧ ¬y
                # A => B эквивалентно not A or B
                # A => B эквивалентно A <= B в питоне
                expr = x and (not z or w) and not y
                if expr == True:
                    print(w,x,y,z,int(expr))

#### А мб это:

A = [0, 1]
for w in A:
    for x in A:
        for y in A:
            for z in A:
                # ((¬z ∨ w) ∧ (¬x ≡ y)) → (x ∧ z)
                expr = ((not z or w) and (not x == y)) <= (x and z)
                if expr == False:
                    print(w,x,y,z,int(expr))

# В любом случае, здесь прослеживается один паттерн:
# Набор значений для перебора задаётся через список [0, 1],
# а затем ссылка на него по имени A используется во вложенных циклах.