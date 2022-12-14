import math


class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def distance(self,k):
        x0 = self.a - k.a
        y0 = self.b - k.b
        return math.sqrt(x0 * x0 + y0 * y0)
for _ in range(int(input())):
    a=[float(x) for x in input().split()]
    x=Point(a[0],a[1])
    y=Point(a[2],a[3])
    z=Point(a[4],a[5])
    n=x.distance(y)
    m=y.distance(z)
    k=x.distance(z)
    if max(n,m,k)*2>=n+m+k:
        print("INVALID")
    else:
        s=math.sqrt((n+m+k)*(n+m-k)*(n-m+k)*(-n+m+k))/4
        print("%.2f"%s)
        