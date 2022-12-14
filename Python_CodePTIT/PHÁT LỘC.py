from operator import le


t=int(input())
while t>0:
    s=input()
    print("YES" if(s[len(s)-1]=='6'and s[len(s)-2]=='8')else "NO")
    t=t-1