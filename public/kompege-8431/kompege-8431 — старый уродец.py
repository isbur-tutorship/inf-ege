f = open('24_8431.txt')
mifile = f.readline()
f.close()
isxod = list(map(str, mifile))

copid = [' ' for _ in range(len(isxod))]

slovar = ['XYZ',
          'XZY',
          'YXZ',
          'YZX',
          'ZXY',
          'ZYX']
offset = -1

for i in range(2, len(isxod)):
    if ((isxod[i-2] + isxod[i-1] + isxod[i]) not in slovar):
        offset -= 1
        if offset < 0:
            copid[i-2] = isxod[i-2]
            copid[i-1] = isxod[i-1]
            copid[i] = isxod[i]
        
    else:
        offset = 2
        copid[i-2] = ' '
        copid[i-1] = ' '
        copid[i] = ' '
        

ans = "".join(copid)
print(max([len(x) for x in ans.split()]))