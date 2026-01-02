def f(s: int, n: int):
    
    if n > 4:
        return -1
    
    if s >= 40:
        return 0
    
    khody = [s + 2, s * 2 - 1]
    
    if any(f(khod, n + 1) == 0 for khod in khody):
       return 1
    
    if all(f(khod, n + 1) == 1 for khod in khody):
        return 2
    
    if any(f(khod, n + 1) == 2 for khod in khody):
        return 3
    
    if all(f(khod, n+1) in (1, 3) for khod in khody):
        return 4
        

for s in range(1, 40):
    if f(s,0) == 3:
        print(3, s)
    if f(s,0) == 4:
        print(4, s)