from operator import truediv
from textwrap import indent
P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while(True):
    x=input().split()
    k=int(x[0])
    if k==0:
        break
    s=x[1]
    tmp=""
    for i in s:
        tmp+=P[(P.index(i)+k)%28]
    print(tmp[::-1])