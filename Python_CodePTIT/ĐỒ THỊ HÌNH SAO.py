n=int(input())
m={}
tmp="Yes"
for i in range(n-1):
    a,b=map(int,input().split())
    if a in m:
        m[a]+=1
    else:
        m[a]=1
    if b in m:
        m[b]+=1
    else:
        m[b]=1
for i in range(1,n+1):
    if(not(i in m) or m[i]!=1 and m[i]!=n-1):
        tmp="No"
        break
print(tmp)
    