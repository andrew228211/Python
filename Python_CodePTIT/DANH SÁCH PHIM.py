class Phim:
    def __init__(self,ma,ten,ngay,so,tl,ngayG):
        self.ma=ma
        self.ten=ten
        self.ngay=ngay
        self.so=so
        self.tl=tl
        self.ngayG=ngayG
n,m=map(int,input().split())
the={}
phim=[]
for i in range(n):
    ma="TL"+"{:03d}".format(i+1)
    tl=input()
    tl=tl.strip()
    the[ma]=tl
for i in range(m):
    ma="P"+"{:03d}".format(i+1)
    tmp=input()
    tmp=tmp.strip()
    tl=the[tmp]
    ngay=input()
    ngayG=ngay[::-1]
    ten=input()
    so=int(input())
    phim.append(Phim(ma,ten,ngay,so,tl,ngayG))
phim.sort(key=lambda x:(x.ngayG,x.ten,-x.so))
for x in phim:
    print(x.ma,x.tl,x.ngay,x.ten,x.so)
    
    