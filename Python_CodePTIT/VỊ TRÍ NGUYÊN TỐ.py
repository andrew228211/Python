from math import fabs


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
def kt(s):
    for i in range(1,len(s)):
        if(f[i]==True and f[int(s[i])]==False):
            return "NO"
        if(f[i]==False and f[int(s[i])]==True):
            return "NO"
    return "YES"
for _ in range(int(input())):
    s=input()
    print(kt(s))
    
