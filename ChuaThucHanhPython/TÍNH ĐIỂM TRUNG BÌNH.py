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
    hoten=input().split()
    ten=" ".join(hoten)
    ten=ten.capitalize().title()
    d1=Decimal(input())
    d2=Decimal(input())
    d3=Decimal(input())
    dtb=d1*3+d2*3+d3*2
    dtb=dtb/8
    dtb=dtb.quantize(Decimal('1.00'),ROUND_HALF_UP)
    #ghi chu quantize dunng de lam tron len tren, duoi
    #1.00 để xác định số phẩy thập phân của số đuọc làm tròn chứa bn số ví dụ 1.00 có 2 số sau dấu phẩy thì só làm tròn có chứa 2 số sau dấy phẩy
    xh=0
    a.append(Diem(ma,ten,dtb,xh))
a.sort(key=lambda X:(-X.dtb))
cnt=1
tmp=a[0].dtb
dem=0
for i in a:
    if tmp==i.dtb:
        dem+=1
    elif tmp>i.dtb:
        cnt=cnt+dem
        tmp=i.dtb
        dem=1
    i.xh=cnt
for i in a:
    print(i.ma,i.ten,i.dtb,i.xh)

