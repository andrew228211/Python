def kt(s):
    if(len(s)<3): return 0
    x=0
    for i in range(len(s)):
        if(int(s[i])>=int(s[i+1])):
            x=i
            break
    if(x==len(s) or x==0): return 0
    tmp=0
    for i in range(x,len(s)-1):
        if(int(s[i])<int(s[i+1])):
            tmp=i
            break
    if(tmp==0): return 1
    return 0
t=int(input())
while(t>0):
    s=input()
    if(kt(s)==1): print("YES")
    else: print("NO")
    t-=1