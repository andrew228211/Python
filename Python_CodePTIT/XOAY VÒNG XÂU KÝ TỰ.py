n=int(input())
a=['']*n
for i in range(n):
    a[i]=input()
m=len(a[0])
s=a[0]
ans=10**9
for j in a:
    s=j
    d=0
    for i in a:
        x=i
        for k in range(m):
            if(x==s):
                d+=k
                break
            x=x[1::]+x[0]     
        if x!=s:
            ans=-1 
    ans=min(d,ans)    
print(ans)