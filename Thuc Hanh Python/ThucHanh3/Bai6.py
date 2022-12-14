from decimal import ROUND_HALF_UP, Decimal


class Diem:
    def __init__(self,ma,ten,dtb,xh):
        self.ma=ma
        self.ten=ten
        self.dtb=dtb
        self.xh=xh
a=[]
for i in range(int(input())):
    ma="SV"+"{:02d}".format(i+1)
    ho=input()
    ho=" ".join(ho.split())
    ten=ho.capitalize().title()
    d1=Decimal(input())
    d2=Decimal(input())
    d3=Decimal(input())
    dtb=d1*3+d2*3+d3*2
    dtb=dtb/8
    dtb=dtb.quantize(Decimal("0.01"),ROUND_HALF_UP)
    xh=0
    a.append(Diem(ma,ten,dtb,xh))
a.sort(key=lambda X:(-X.dtb,X.ma))
tmp=10
h=1
tmp2=h
for x in a:
    if x.dtb<tmp:
        tmp2=h
        x.xh=tmp2
        tmp=x.dtb
        h+=1
    elif x.dtb==tmp:
        x.xh=tmp2
        h+=1
for x in a:
    print(x.ma,x.ten,x.dtb,x.xh)
