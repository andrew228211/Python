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
a=list(map(int,input().split()))
m={}
for i in a :
    if f[i] == True :
        if i in m : continue
        else :
            print(i,a.count(i))
            m[i] = 1