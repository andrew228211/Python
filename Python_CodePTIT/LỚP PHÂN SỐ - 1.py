import math


class Phanso:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def rutgon(self):
        k=math.gcd(self.a,self.b)
        self.a=int(self.a/k)
        self.b=int(self.b/k)
    def out(self):
        print(self.a,"/",self.b,sep="")
a,b=map(int,input().split())
f=Phanso(a,b)
f.rutgon()
f.out()
        