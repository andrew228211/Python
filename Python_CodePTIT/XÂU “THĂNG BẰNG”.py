import math

def ktra(n):
    a=n[::-1]
    for i in range(1,len(n)-1):
        if abs(ord(n[i])-ord(n[i-1]))!=abs(ord(a[i])-ord(a[i-1])):
            return 0
    return 1
t=int(input())
for i in range(t):
    n=input()
    if ktra(n):
        print("YES")
    else:
        print("NO")