import math


t=int(input())
while t>0:
    s=input()
    Min=999999
    sum=0
    flag=9999999
    j=0
    while(j<len(s)):
        for i in range(j,len(s)):
            j=j+1
            if(s[i]>='a'and s[i]<='z'):
                break
            else:
                sum=sum*10+int(s[i])
                flag=sum
        Min=min(Min,flag)
        sum=0
        flag=999999
    Min=min(Min,flag)
    print(Min)
    t=t-1
