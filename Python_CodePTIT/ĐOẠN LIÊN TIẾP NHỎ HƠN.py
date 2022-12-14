from queue import Empty
t=int(input())
while(t>0):
    n=int(input())
    a=list(map(int,input().split()))
    b=[1 for i in range(n)] 
    st=[]
    for i in range(n):
        if(len(st)>0):
            x=st.pop()          
            while(a[x]<=a[i]):            
                b[i]=b[i]+b[x]   
                if(len(st)>0):
                    x=st.pop()
                else:
                    break
            if(a[x]>a[i]):
                st.append(x)
        st.append(i)          
    for i in range(n):
        print(b[i],end=" ")
    print()
    t-=1