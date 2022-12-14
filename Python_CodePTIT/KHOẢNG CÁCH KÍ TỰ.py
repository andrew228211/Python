def kt(s,s1):
    for i in range(1,len(s)):
        if(abs(ord(s[i])-ord(s[i-1]))!=abs(ord(s1[i])-ord(s1[i-1]))):
            return 0
    return 1
t=int(input())
while(t>0):
    s=input()
    s1=s[::-1]
    if(kt(s,s1)==1): print("YES")
    else: print("NO")
    t-=1