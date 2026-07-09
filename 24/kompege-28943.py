#kompege-28943

f = open("24_28943.txt")
s = f.read()
s = s.split("20")
minn = 100
for i in range(len(s) - 27):
    curs = "20".join(s[i:i+27])
    n = len(curs)
    if (curs[-1] in "AEIUYO") and all(not (l in curs[:-1]) for l in "AEIYUO"):
        minn = min(minn, n) 
    
print(minn)