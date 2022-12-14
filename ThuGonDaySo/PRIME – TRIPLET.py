from operator import truediv


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
t=int(input())
Sang()
a=[]
for i in range(2,1000005):
    if(f[i]==True):
        a.append(i)
while t>0:   
    n=int(input())
    cnt=0
    for i in a:
        if(i>n):
            break
        if(i+6<n):
            if(f[i+2]==True and f[i+6]==True) or (f[i+4]==True and f[i+6]==True):
                cnt+=1
    print(cnt)
    t=t-1