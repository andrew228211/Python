for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[[0]*n]*m
    b=[]
    for i in range(n):
        a[i]=[int(x) for x in input().split()]
    for i in range(m) :
        x = []
        for j in range(n) :
            x.append(a[j][i])
        b.append(x)
    for i in range(n) :
        for j in range(n) :
            s = 0
            for z in range(m) :
                s += a[i][z] * b[z][j]
            print(s, end = ' ')
        print()
    
        
    