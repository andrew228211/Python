import math
t=int(input())
while t>0:
    s=input()
    Max=0
    sum=0
    j=0
    while(j<len(s)):
        for i in range(j,len(s)):
            j=j+1
            if(s[i]>='a'and s[i]<='z'):
                break
            else:
                sum=sum*10+int(s[i])
        Max=max(Max,sum)
        sum=0
    print(max(Max,sum))
    t=t-1
