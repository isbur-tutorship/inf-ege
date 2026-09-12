from itertools import product
otv = 0
for i in product('0123456789ab', repeat=5):
    if i[0] != '0':
        necet = [x for x in i if x in '13579b']
        if len(set(necet)) == 1 and len(necet) == 3:
            if necet[0]*3 in ''.join(i):
                otv += 1
print(otv)