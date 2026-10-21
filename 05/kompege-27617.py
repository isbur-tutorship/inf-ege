# kompege-27617 

for N in range(1000)
    R=bin(N)
    R=R[2]
    if N%3==0
        R=R+R[-3]
    if N%3!=0
        a=bin(int(N%3)3)[2]
        R=R+a
    R=int(R,2)
    print(N, R, abs(R-130))
    
# Экспериментально выявлено, что для сложных вопросов проще смотреть глазами