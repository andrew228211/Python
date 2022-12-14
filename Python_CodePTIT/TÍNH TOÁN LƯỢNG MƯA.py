class Mua:
    def __init__(self,ma,ten,start,end,tong):
        self.ma=ma
        self.ten=ten
        a=[int(x) for x in start.split(":")]
        b=[int(x) for x in end.split(":")]
        self.thoigian=b[0]*60+b[1]-a[0]*60-a[1]
        self.tong=tong
m={}
h=1
ds=[]
luuTong={}
for i in range(int(input())):
    ten=input()
    start=input()
    end=input()
    tong=int(input())
    id=h
    if ten in m:
        id=m[ten]
    else:
        m[ten]=h
        id=h
        h+=1
    ma="T"+"{:02d}".format(id)
    ds.append(Mua(ma,ten,start,end,tong))
for i in m.keys():
    sum=0
    tg=0
    ma=""
    for x in ds:
       if(i==x.ten):
           sum+=x.tong
           tg+=x.thoigian
           ma=x.ma
    k=tg/60
    print(ma,i,"%.2f"%(sum/k))