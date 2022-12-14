a=[1]*1025
def nt():
    a[0]=0
    a[1]=0
    for i in range(2,33):
       if a[i]==1:
           j=i*i
           while(j<=1024):
               a[j]=0
               j=j+i
nt()
n,m=map(int,input().split())
Max=0
b=[[0]*m for i in range(n)]
for i in range(n):
    b[i]=[int(x) for x in input().split()]
    for j in b[i]:
        if(a[j]==1):
            Max=max(Max,j)
if(Max==0):
    print("NOT FOUND")
else:
    print(Max)
    for i in range(n):
        for j in range(m):
            if b[i][j]==Max:
                print("Vi tri [{0}][{1}]".format(i,j))
          