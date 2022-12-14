f=[True for i in range(1000005)]
def Sang():
    f[0]=False
    f[1]=False
    for i in range(2,1000):
        if(f[i]==True):
            j=i*i
            while(j<1000001):
                f[j]=False
                j=j+i
Sang()
n,x=map(int,input().split())
cnt=0
print(x,end=" ")
for i in range(1000001):
    if(f[i]==True):
        x+=i
        print(x,end=" ")
        cnt+=1
    if(cnt==n): break