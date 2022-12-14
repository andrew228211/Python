from ctypes import c_char
from ctypes.wintypes import CHAR
from gettext import find


for _ in range(int(input())):
    n,k=map(int,input().split())
   # print(chr(find(n,k)+ord('A')-1))
    for i in range(1,n+1):
        x=pow(2,i)
        if(k%x==x/2):
           print(chr(i+64))
           break