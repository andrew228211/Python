class ThoiGian:
    def __init__(self,ma,ten,gio):
        self.ma=ma
        self.ten=ten
        self.gio=gio
a=[]
for _ in range(int(input())):
    ma=input()
    ten=input()
    v=input()
    r=input()
    x=[int(i) for i in v.split(":")]
    y=[int(i) for i in r.split(":")]
    gio=y[0]*60+y[1]-x[0]*60-x[1]
    a.append(ThoiGian(ma,ten,gio))
a.sort(key=lambda X:X.gio,reverse=True)
for i in a:
    hour=i.gio//60
    phut=i.gio-hour*60
    print("{0} {1} {2} gio {3} phut".format(i.ma,i.ten,hour,phut))