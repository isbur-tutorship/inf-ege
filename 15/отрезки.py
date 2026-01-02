def P(x):
    return 3 <= x <= 38
def Q(x):
    return 21 <= x <= 57
def A(x):
    return True
def expr(x):
    return ((Q(x)) <= (P(x))) <= (not (A(x)))
# ((х ∈ Q) → (х ∈ Р)) → ¬(х ∈ A)
for x in range(0,61):
    if expr(x):
        print("#", end = "")
    else:
        print("_", end = "")
    if x % 5 == 0:
        print(f"|{x+1}|", end = "")

print()
print(expr(38))
print(expr(38.2))
print(expr(57))
print(expr(57.8))