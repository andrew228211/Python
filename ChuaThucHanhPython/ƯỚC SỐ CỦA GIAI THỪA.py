#9!=9*8*7*6*5*4*3*2
t=int(input())
#ctrl+Alt+B
for _ in range(t):
    cnt=0
    n,p=map(int,input().split())
    for i in range(2,n+1):
        tmp=i
        while(tmp%p==0):
            cnt+=1
            tmp/=p
    print(cnt)