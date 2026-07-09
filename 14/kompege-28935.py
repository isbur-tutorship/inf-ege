#kompege-28935
for x in sorted("1234567890qwertyuiopasdfghjklzxcvbnm")[:23]:
    n = int("761"+x+"035", 23) + int("338"+x+"932", 23)
    if n % 22 == 0:
        print(x, n // 22)