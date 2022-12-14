from dataclasses import replace
import string


t=int(input())
while(t>0):
    p,q=map(int,input().split())
    Min=min(p,q)
    Max=max(p,q)
    try:
        s=input().split()
        x1=s[0]
        x2=s[1]
    except:
        x2=input()
    tong=int(x1.replace(str(Max),str(Min)))+int(x2.replace(str(Max),str(Min)))
    sum2=int(x1.replace(str(Min),str(Max)))+int(x2.replace(str(Min),str(Max)))
    print(tong,sum2)
    t=t-1