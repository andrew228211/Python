from datetime import date, datetime


class HoaDon:
    def __init__(self,ma,ten,soPhong,soNgay,tt):
        self.ma=ma
        self.ten=ten
        self.soPhong=soPhong
        self.soNgay=soNgay
        self.tt=tt
ds=[]
for i in range(int(input())):
    ma="KH"+"{:02d}".format(i+1)
    ten=input()
    sP=input()
    soPhong=int(sP)
    a=[int(x) for x in input().split("/")]
    b=[int(x) for x in input().split("/")]
    f_date=date(a[2],a[1],a[0])
    l_date=date(b[2],b[1],b[0])
    soNgay=int((l_date-f_date).days)+1
    chiphi=int(input())
    tang=int(sP[0])
    tt=0
    if tang == 1:
        tt=chiphi+25*soNgay
    elif tang==2:
        tt=chiphi+34*soNgay
    elif tang==3:
        tt=50*soNgay+chiphi
    else:
        tt=80*soNgay+chiphi
    ds.append(HoaDon(ma,ten,soPhong,soNgay,tt))
ds.sort(key=lambda X:-X.tt)
for i in ds:
    print(i.ma,i.ten,i.soPhong,i.soNgay,i.tt)