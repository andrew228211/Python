class MonThi:
    def __init__(self,ma,ten,ht):
        self.ma=ma
        self.ten=ten
        self.ht=ht
a=[]
for i in range(int(input())):
    ma=input()
    ten=input()
    ht=input()
    a.append(MonThi(ma,ten,ht))
a.sort(key=lambda X:X.ma)
for i in a:
    print(i.ma,i.ten,i.ht)