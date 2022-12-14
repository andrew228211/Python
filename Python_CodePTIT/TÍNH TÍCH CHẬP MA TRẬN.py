for _ in range(int(input())):
    n,m=map(int,input().split())
    a=[[0]]*(n+1)
    for i in range(1,n+1):
        a[i]=[int(x) for x in input().split()]
    b=[[0]]*3
    for i in range(3):
        b[i]=[int(x) for x in input().split()]
    sum=0
    for i in range(n):
        for j in range(m):
            try:
                x=b[0][0]*a[i][j]+b[0][1]*a[i][j+1]+b[0][2]*a[i][j+2]+b[1][0]*a[i+1][j]+b[1][1]*a[i+1][j+1]+b[1][2]*a[i+1][j+2]+b[2][0]*a[i+2][j]+b[2][1]*a[i+2][j+1]+b[2][2]*a[i+2][j+2]
                sum+=x
            except:
                continue
    print(sum)