fibo=[0,1,1]
for i in range(3,93):
    fibo.append(fibo[i-2]+fibo[i-1])
for t in range(int(input())):
    a,n=map(int,input().split())
    for i in range(a,n+1):
        print(fibo[i],end=" ")
    print()
