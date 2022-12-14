from cmath import sqrt


t=int(input())
while t>0:
    n=int(input())
    a=[]
    for i in range(2,n):
        a.append(i)
    for i in a:
        if(n%i==0):
            a.remove(i)
            tmp=i
            x=2
            while tmp*x<=n:
                if(tmp*x in a): a.remove(tmp*x)
                x=x+1
    ans=len(a)+1
    if(ans<2): print("NO")
    else:
        flag=1
        for i in range(2,ans):
            if(ans%i==0): 
                flag=0
                break
        print("NO" if(flag==0) else "YES")   
    t=t-1