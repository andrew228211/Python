from collections import deque
from inspect import _empty, stack
from pickletools import StackObject
import queue
for _ in range(int(input())):
    s=input()
    st=[]
    h=1
    for i in range(len(s)):
        if s[i]=='(':
            st.append(h)
            print(h,end=" ")
            h+=1
        elif s[i]==')':
            print(st.pop(),end=" ")
    print()
            
    