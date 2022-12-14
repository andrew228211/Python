import math
from cmath import sqrt
def f(x):
    if(x<2): return 0
    for i in range(2,int(sqrt(x).real)+1):
        if x%i==0: return 0
    return 1
t=int(input())
while(t>0):
    a,b=map(int,input().split())
    usc=math.gcd(a,b)
    x=0
    while(usc>0):
        x=x+usc%10
        usc=usc//10
    if(f(x)==1): print("YES")
    else: print("NO")
    t-=1