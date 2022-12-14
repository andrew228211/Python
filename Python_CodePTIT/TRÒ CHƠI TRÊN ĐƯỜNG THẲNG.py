class Diem:
    def __init__(self,x,y):
        self.x=x
        self.y=y     
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    c=[int(x) for x in input().split()]
    ds=[]
    for i in range(n):
        ds.append(Diem(a[i],c[i]))
    ds.sort(key=lambda X:X.y)
    Min=0
    flag=0
    for i in ds:
        if i.x%2==0:
            Min+=i.y
            flag=1
            break
    if flag==0:
        print(-1)
    else:
        for i in ds:
            if i.x%2==1:
                Min+=i.y
                flag=0
                break
        if flag==1:
            print(-1)
        else:
            print(Min)
        