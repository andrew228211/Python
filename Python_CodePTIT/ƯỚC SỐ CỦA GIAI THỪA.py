
for _ in range(int(input())):
    n,p=map(int,input().split())
    cnt=0
    for i in range(2,n+1):
        x=i
        while(x%p==0):
            x=x/p
            cnt+=1
    print(cnt)