f='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for _ in range(int(input())):
    n,b=map(int,input().split())
    s=''
    while(n>0):
        s=f[n%b]+s
        n=n//b
    print(s)