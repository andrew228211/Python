import functools
from imaplib import Int2AP


class XH:
    def __init__(self,name,dung,sai):
        self.name=name
        self.dung=dung
        self.sai=sai
def cmp(x,y):
    if x.dung<y.dung:
        return 1
    elif x.dung==y.dung:
        if x.sai>y.sai:
            return 1
        elif x.sai==y.sai:
            if(x.name>y.name):
                return 1
            else: return -1
        else: return -1
    else:
        return -1
t=int(input())
a=[]
while(t>0):
    name=input()
    dung,sai=map(int,input().split())
    a.append(XH(name,dung,sai))
    t-=1
a=sorted(a,key=functools.cmp_to_key(cmp))
for i in a:
    print(i.name,i.dung,i.sai)