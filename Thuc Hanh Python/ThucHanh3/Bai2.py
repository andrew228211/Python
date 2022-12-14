m,n=map(int,input().split())
a=[[0]*n for x in range(m)]
b=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
q=[]
for i in range(m):
    a[i]=[int(x) for x in input().split()]
    for j in range(n):
        if a[i][j] == -1:
            q.append([i,j])
s=0
while(len(q)>0):
    u=q[0]
    q.pop(0)
    for i in b:
        x=i[0]+u[0]
        y=i[1]+u[1]
        if x>=0 and x<m and y>=0 and y<n:
            if a[x][y]!=0:
                s+=a[x][y]
                a[x][y]=0
print(s)