# Старый вариант 25го
# https://3.shkolkovo.online/solve-variant/fGRwspSJGGCZthkgHfgBSbn/self-checking

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


c = 0
for n in range(8996452+1, 8996452+1000000):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and str(i).count("3") == 2 and str(n // i).count("3") == 2 and isPrime(i) and isPrime(n // i):
            print(n, max(i, n // i))
            c += 1
            break
    if c == 5:
        break

# 9001609,24133 9002887,38639 9006149,38653 9012167,3853 9012373,23531