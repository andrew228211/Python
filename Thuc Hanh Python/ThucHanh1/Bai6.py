class Hoadon:
    def __init__(self,ma,ten,tong):
        self.ma=ma
        self.ten=ten
        self.tong=tong
    def out(self):
        print(self.ma,self.ten,self.tong)
a=[]
for i in range(int(input())):
    ma="KH"+"{:02d}".format(i+1)
    ten=input()
    cu=int(input())
    moi=int(input())
    hieu=moi-cu
    tong=0
    if hieu<=50:
        tong=hieu*100+100*hieu*0.02
    elif hieu<=100:
        tong=50*100+(hieu-50)*150
        tong+=tong*0.03
    else:
        tong=50*100+50*150+(hieu-50-50)*200
        tong+=tong*0.05
    a.append(Hoadon(ma,ten,round(tong)))
a.sort(key=lambda X:X.tong,reverse=True)
for x in a:
    x.out()