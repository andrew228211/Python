from cmath import sqrt
import math
from turtle import end_fill


def kt(s):
    if(s<2): return 0
    for i in range(2,int(sqrt(s).real)+1):
        if(s%i==0): 
            return 0
    return 1
# for _ in range(int(input())):
#     s=input()
#     print(kt(s))
n,m=map(int,input().split())
a=[[]]
b=[]
for i in range(n):
    b=[int(x) for x in input().split()]
    a.append(b)
for i in range(1,n+1):
    for j in range(0,m):
        if(kt(a[i][j])==1):
            print(1,end=" ")
        else: print(0,end=" ")
    print()