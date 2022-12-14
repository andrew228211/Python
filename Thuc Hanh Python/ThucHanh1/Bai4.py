while True:
    a=[int(x) for x in input().split()]
    if(a[0]==0 and a[1]==0 and a[2]==0 and a[3]==0):
        break
    cnt=0
    if(a[0] == a[1] and a[1]==a[2] and a[2]==a[3]):
        print(cnt)
    else:
        while True:
            tmp=a[0]
            for i in range(len(a)-1):
                a[i]=abs(a[i]-a[i+1])
            a[3]=abs(a[3]-tmp)
            cnt+=1
            if(a[0] == a[1] and a[1]==a[2] and a[2]==a[3]):
                print(cnt)
                break
        
        