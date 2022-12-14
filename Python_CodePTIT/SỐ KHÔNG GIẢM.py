def Kt(s):
    for i in range(len(s)-1):
        if(int(s[i+1])<int(s[i])):
            print("NO")
            return
    print("YES")
    return
t=int(input())
while t>0:   
    s=input()
    Kt(s)
    t=t-1