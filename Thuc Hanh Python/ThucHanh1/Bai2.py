from math import gcd


t=int(input())
for _ in range(t):
    n=input()
    a=n[::-1]
    x=int(n)
    y=int(a)
    if(gcd(x,y)==1):
        print("YES")
    else:
        print("NO")