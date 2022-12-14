from operator import truediv


f=[True for i in range(1000005)]
def doi(y):
    x=0
    while(y>0):
        u=y%10
        x=x*10+u
        y=y//10
    return x
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
        if(i!=doi(i) and f[doi(i)]==True and doi(i)>i and doi(i)<n):
            print(i,doi(i),end=' ')    
    print()
    t=t-1