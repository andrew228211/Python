for t in range(int(input())):
    s=int(input())
    i=str(s)
    cnt=0
    if(s%7==0): print(s)
    else: 
        while(cnt<1001):
            x=int(i)+int(i[::-1])
            i=str(x)
            if(x%7==0): break
        if cnt==1000: print(-1)
        else: print(i)