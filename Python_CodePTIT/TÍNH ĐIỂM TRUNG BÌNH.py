t=int(input())
a=list(map(float,input().split()))
x=min(a)
y=max(a)
cnt=0
sum=0
for i in a:
    if(i!=x and i!=y):
        sum+=i
        cnt+=1
z=sum/cnt
print("%.2f"%z)