class Chuyen:
    def __init__(self,ma,ten,lop,dcc):
        self.ma=ma
        self.ten=ten
        self.lop=lop
        self.dcc=dcc
class Tinh:
    def __init__(self,ma,dd):
        self.ma=ma
        self.dd=dd
a=[]
t=int(input())
for i in range(t):
    ma=input()
    ten=input()
    lop=input()
    dcc=10
    a.append(Chuyen(ma,ten,lop,dcc))
b=[]
for i in range(t):
    n=input().split()
    ma=n[0]
    s=n[1]
    dd=10
    for i in s:
        if(i=='v'):
            dd-=2
        elif i=='m':
            dd-=1
        if dd<=0:
            break
    b.append(Tinh(ma,dd))
for i in a:
    for j in b:
        if i.ma==j.ma:
            i.dcc=j.dd
            break
for i in a:
    h=""
    if i.dcc==0:    
        h="KDDK"
        print(i.ma,i.ten,i.lop,i.dcc,h)
    else:
        print(i.ma,i.ten,i.lop,i.dcc)