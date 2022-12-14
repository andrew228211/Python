
n=int(input())
a=[]
ngang=[0]*n
doc=[0]*n
for i in range(n):
    a.append(input())
for i in range(n):
    for j in range(n):
        if(a[i][j]=='C'):
            ngang[i]+=1
            doc[j]+=1
sum=0
for i in range(n):
    sum+=ngang[i]*(ngang[i]-1)//2
    sum+=doc[i]*(doc[i]-1)//2
print(sum)