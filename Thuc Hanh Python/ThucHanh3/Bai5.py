class ThoiGian:
    def __init__(self,ma,ten,thoigian):
        self.ma=ma
        self.ten=ten
        self.thoigian=thoigian
a=[]
for i in range(int(input())):
    ma=input()
    ten=input()
    vao=[int(x) for x in input().split(":")]  
    ra=[int(x) for x in input().split(":")]   
    tong=ra[0]*60+ra[1]-vao[0]*60-vao[1]
    a.append(ThoiGian(ma,ten,tong))
a.sort(key=lambda X:X.thoigian,reverse=True)
for i in a:
    gio=i.thoigian//60
    phut=i.thoigian-gio*60
    thoigian="{0} gio {1} phut".format(gio,phut)
    print(i.ma,i.ten,thoigian)