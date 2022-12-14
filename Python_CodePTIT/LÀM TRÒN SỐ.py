
t=int(input())
while t>0:
        s=input()
        n=int(s)
        if(n>10):
            for i in range(len(s)-1):
            #   print(n%(10**(i+1))," ",5*(10**i))
              if(n%(10**(i+1))>=5*(10**i)):
                n=n+10**(i+1)-n%(10**(i+1))
              else:
                n=n-n%(10**(i+1))
            print(n)
        else: print(n)
        t=t-1