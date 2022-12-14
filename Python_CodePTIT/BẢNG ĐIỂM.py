from decimal import ROUND_HALF_UP, Decimal
id=1
class HocSinh:
    ma="HS"
    dtb=0
    xepLoai=""
    def __init__(self,ten,diem):
        global id
        self.ma+="{:02d}".format(id)
        id+=1
        self.ten=ten
        x=diem[0]*2+diem[1]*2
        for i in range(2,10):
            x+=diem[i]
        x/=12
        if x < 5 : self.xepLoai = 'YEU'
        elif x < 7 : self.xepLoai = 'TB'
        elif x < 8 : self.xepLoai = 'KHA'
        elif x < 9 : self.xepLoai = 'GIOI'
        else : self.xepLoai = 'XUAT SAC'
        self.dtb = x.quantize(Decimal('0.1'), ROUND_HALF_UP)
    def output(self) :
        print(self.ma, self.ten, self.dtb, self.xepLoai)
a=[]
for _ in range(int(input())):
    name=input()
    diem = [Decimal(x) for x in input().split()]
    a.append(HocSinh(name,diem))
a=sorted(a,key=lambda x :(-x.dtb,x.ma))
for i in a:
    i.output()
    