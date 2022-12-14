class Mon:
    def __init__(self,ma,ten,ht):
        self.ma=ma
        self.ten=ten
        self.ht=ht  
a=[]
for _ in range(int(input())):
    ma=input()
    ten=input()
    ht=input()
    a.append(Mon(ma,ten,ht))
a.sort(key=lambda x:x.ma)
for i in a:
    print(i.ma,i.ten,i.ht)