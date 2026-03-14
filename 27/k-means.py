from math import dist

# A = [[float(y) for y in x.split()] for x in open("27_A_23766.txt")]
A = [[float(y) for y in x.split()] for x in open("27_B_23766.txt")]

minX = min(M[0] for M in A)
maxX = max(M[0] for M in A)
minY = min(M[1] for M in A)
maxY = max(M[1] for M in A)

# centroids = [(minX, minY), (maxX, maxY)]
init_centroids = [(minX, minY), (minX, maxY), (maxX, maxY)]

def f(centroids):

    while True:
        C = []
        for x, y in A:
            D = []
            for xc, yc in centroids:
                D.append(dist((x,y),(xc,yc)))
            C.append(D.index(min(D)))
        # print(C)
        new_centroids = []
        for i in range(len(centroids)):
            xm, ym = 0, 0
            cnt = 0
            for j in range(len(A)):
                if C[j] == i:
                    xm += A[j][0] # += x
                    ym += A[j][1] # += y
                    cnt += 1
            
            if cnt == 0:
                new_centroids.append(centroids[i])
                continue
            
            xm /= cnt
            ym /= cnt
            
            new_centroids.append([xm, ym])
        
        if new_centroids == centroids:
            break
        
        centroids = new_centroids
    
    return centroids, C

centroids, C = f(init_centroids)

# print(centroids)

pairs = []

for i,p in enumerate(A):
    c = C[i]
    pairs.append((dist(p, centroids[c]), i))

pairs.sort()

# cut = int(len(A)*0.99)
cut = -3

A = [A[i] for _,i in pairs[:cut]]

centroids, C = f(init_centroids)

# print([C.count(i) for i in range(3)])
# [407, 113, 100]
print(dist(centroids[0], centroids[2])*10**4, pairs[-4][0]*10**4)

# print(centroids)