from math import gcd
t=int(input())
while(t>0):
    x=input()
    y=x[::-1]
    usc=gcd(int(x),int(y))
    print("YES" if(usc==1) else "NO")   
    t-=1
