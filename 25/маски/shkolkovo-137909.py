# 25ое
# https://3.shkolkovo.online/catalog/13059/137909

from fnmatch import *

for n in range(317, 10**8+1, 317):
    if fnmatch(str(n), "12??1*56"):
        print(n, n // 317)