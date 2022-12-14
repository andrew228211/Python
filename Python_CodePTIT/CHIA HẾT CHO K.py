from re import I


def Kiemtra(a,k,b):
    x=-1 
    if a>k: 
        t=k*2
        if t+a>b:
            print(-1)
            return
        else:
            x=t-a
    else:
        if(k>b):
            print(-1)
            return
        else:
            x=k-a
    if x==-1:
        print(-1)
        return
    while x+a<=b:
        print(x,end=' ')
        x=x+k
    return
s=input().split()
a=int(s[0])
k=int(s[1])
b=int(s[2])
Kiemtra(a,k,b)