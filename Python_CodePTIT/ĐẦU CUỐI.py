t=int(input())
while t>0:
    s=input()
    print("YES" if(s[0]==s[len(s)-2])and(s[1]==s[len(s)-1])else "NO")
    t=t-1