from bisect import bisect
from sqlite3 import Binary


t=int(input())
while t>0:   
    n=int(input())
    a=list(map(int,input().split()))
    cnt=0
    a.sort()
    for i in range(0,n-3):
        l=i+1
        r=n-1
        x=a[i]
        while(l<r):
            if(x+a[l]+a[r]==0):
                cnt=cnt+1
                l=l+1
            elif(x+a[l]+a[r]<0): l=l+1
            else: r=r-1
    print(cnt)
    t=t-1