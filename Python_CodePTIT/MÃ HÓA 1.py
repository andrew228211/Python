t=int(input())
while t>0:
    n=input()
    n=n+"."
    x=""
    tmp=""
    cnt=1
    for i in range(0,len(n)-1):
        if n[i]!=n[i+1]:
            x=x+str(cnt)+n[i]
            cnt=1
        else:
            cnt+=1
    print(x)
    t-=1