from collections import deque
from inspect import _empty, stack
from pickletools import StackObject
import queue
n=int(input())
a=input().split()
s=[]
for i in range(n):
    if s==[]:
        s.append(int(a[i]))
    else:
        t=int(a[i])
        x=s.pop()
        s.append(x)
        if (t+x)%2==0: 
            s.pop()
        else:
            s.append(t)
print(len(s))

