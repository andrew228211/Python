from operator import truediv
f=[]
f.append(1)
f.append(1)
f.append(2)
for i in range (3,10):
    f.append(f[i-1]*i)
def tach(y):
    x=0
    z=y
    while(y>0):
        u=y%10
        x=x+f[u]
        y=y//10
        if(x>z): 
            return "No"
    if(x==z): 
        return "Yes"
    return "No"
t=int(input())
while t>0:   
    n=int(input())
    print(tach(n))
    t=t-1