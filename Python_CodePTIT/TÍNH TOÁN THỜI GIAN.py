class Game:
    def __init__(self,ma,ten,thoigian):
        self.ma=ma
        self.ten=ten
        self.thoigian=thoigian
ds=[]
for _ in range(int(input())):
    ma=input()
    ten=input()
    a=[int(x) for x in input().split(":")]
    b=[int(x) for x in input().split(":")]
    thoigian=b[0]*60+b[1]-a[0]*60-a[1]
    ds.append(Game(ma,ten,thoigian))
ds.sort(key=lambda X:X.thoigian,reverse=True)
for x in ds:
    print(x.ma,x.ten,end=" ")
    h=x.thoigian//60
    p=x.thoigian-60*h
    print(h,"gio",p,"phut")
    

        