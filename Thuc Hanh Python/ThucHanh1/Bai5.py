from math import gcd


class PhanSo:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def rutgon(self):
        u=gcd(self.a,self.b)
        self.a=int(self.a/u)
        self.b=int(self.b/u)
        print("{0}/{1}".format(self.a,self.b))
x,y=map(int,input().split())
p=PhanSo(x,y)
p.rutgon()