from decimal import Rounded
import math
t=int(input())
while(t>0):
    a,b,c=map(float,input().split())
    x=c/a
    z=math.log(x,(1+b/100))
    print(int(z)+1)
    t-=1