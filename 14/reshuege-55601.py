# y4y + y65 = xz23
# p - неизвестное основание системы

# Обобщённая функция перевода из системы счисления с основанием p в десятичную.
def f(x: str, p: int) -> int:
    s = 0
    for i in range(len(x)):
        s += int(x[len(x) - 1 - i]) * p**i
    return s

for p in range(7, 10):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                a = f"{y}4{y}"
                b = f"{y}65"
                c = f"{x}{z}23"
                if f(a, p) + f(b, p) == f(c, p):
                    print(x, y, z, p)
                    print(f(f"{x}{y}{z}", p))
            
