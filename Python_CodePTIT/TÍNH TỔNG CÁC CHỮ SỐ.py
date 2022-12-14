for _ in range(int(input())):
    s=input()
    a=[]
    sum=0
    for i in range(len(s)):
        if(s[i]>='0'and s[i]<='9'):
            sum+=int(s[i])
        else:
            a.append(s[i])
    a.sort()
    for x in a:
        print(x,end="")
    print(sum)