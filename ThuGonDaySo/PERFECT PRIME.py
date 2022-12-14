from cmath import sqrt
from operator import truediv
import math
def f(x):
    if(x<2): return 0
    for i in range(2,int(sqrt(x).real)):
        if x%i==0: return 0
    return 1

def doi(y):
    x=0
    sum=0
    while(y>0):
        u=y%10
        x=x*10+u
        sum=sum+u
        if(f(u)==0): return 1
        y=y//10
    if(f(sum)==0): return 1
    return x
t=int(input())
while t>0:   
    i=int(input())
    cnt=0
    if(f(i)==1 and f(doi(i))==1):
        print("Yes")
    else:  
     print("No")
    t=t-1