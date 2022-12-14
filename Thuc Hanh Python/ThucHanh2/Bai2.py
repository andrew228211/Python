from cmath import sqrt

a=[1]*1001
def nt():
    a[0]=0
    a[1]=0
    for i in range(2,31):
       if a[i]==1:
           j=i*i
           while(j<=900):
               a[j]=0
               j=j+i
def kt(n):
    for i in range(0,len(n)):
        if(a[i]==0 and a[int(n[i])]!=0):
            return "NO"
        if(a[i]==1 and a[int(n[i])]!=1):
            return "NO"
    return "YES"
nt()
for _ in range(int(input())):
    s=input()
    print(kt(s))
    