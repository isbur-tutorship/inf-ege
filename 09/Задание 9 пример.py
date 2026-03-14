f = open("a6uftdIR6EM.csv")
A = f.readlines()

for row in A:
    row = row.split(',')
    row = [int(x) for x in row]
    
    if row == sorted(row) and (max(row) - min(row)) < (sum(row) - min(row) - max(row)):
        p = 1
        for x in row:
            p *= x
        print(p)
        break
        

    
    

