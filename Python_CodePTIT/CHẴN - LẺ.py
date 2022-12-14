import math
def Tong(n):
    s=str(n)
    sum=0
    for i in range(len(s)-1):
        if(abs(int(s[i])-int(s[i+1]))!=2):
            return 0
        sum=sum+int(s[i])
    sum+=int(s[len(s)-1])
    if(sum%10!=0): return 0
    return 1
t=int(input())
while(t>0):
    n=int(input())
    if(Tong(n)==0): print("NO")
    else: print("YES")
    t-=1