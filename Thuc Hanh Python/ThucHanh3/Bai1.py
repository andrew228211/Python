for _ in range(int(input())):
    cnt=0
    n,p=map(int,input().split())
    for i in range(2,n+1):
        x=i
        while(x%p==0):
            x=x/p
            cnt+=1
    print(cnt)