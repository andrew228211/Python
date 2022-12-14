id=1
class Hoadon:
    ma="KH"
    def __init__(self,ten,moi,cu):
        global id
        self.ten=ten
        self.moi=moi
        self.cu=cu
        self.ma+="{:02d}".format(id)
        id+=1
        sub=cu-moi
        if sub<=50:
            sub=sub*100
            sub=sub+sub*0.02
        elif sub<=100:
            sub=50*100+(sub-50)*150
            sub=sub+sub*0.03
        elif sub>100:
            sub=50*100+50*150+(sub-50-50)*200
            sub=sub+sub*0.05
        self.tien=round(sub)
    def output(self):
        print(self.ma,self.ten,self.tien)
a=[]
for _ in range(int(input())):
    ten=input()
    moi=int(input())
    cu=int(input())
    a.append(Hoadon(ten,moi,cu))
a.sort(key=lambda X:X.tien,reverse=True)
for x in a:
    x.output()
    