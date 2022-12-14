
import math


t=int(input())
a=sorted(list(map(int,input().split())))
for i in range(t):
    for j in range(i+1,t):
        if math.gcd(a[i],a[j])==1:
            print(a[i],a[j])


