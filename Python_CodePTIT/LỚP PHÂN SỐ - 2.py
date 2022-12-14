import math


class Phanso:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def rutgon(self):
        k=math.gcd(self.a,self.b)
        self.a=int(self.a/k)
        self.b=int(self.b/k)
    def add(self,x):
        tu=self.a*x.b+x.a*self.b
        mau=x.b*self.b
        self.a=tu
        self.b=mau
    def out(self):
        print(self.a,"/",self.b,sep="")
f = [int(x) for x in input().split()]
x=Phanso(f[0],f[1])
y=Phanso(f[2],f[3])
x.add(y)
x.rutgon()
x.out()
        