t=int(input())
e=10**9
for _ in range(t):
    n=int(input())
    s=input()
    x,y,z=e,e,e
    n=len(s)//3
    while(s[n]!=' '):
        n-=1
    a=s[:n]
    s=s[n:]
    for i in map(int,a.split()):
        if i<=x:
            z,y,x=y,x,i
        elif i<=y:
            z,y=y,i
        elif i<=z:
            z=i
    n=len(s)//2
    while(s[n]!=' '):
        n-=1
    for i in map(int,s[:n].split()):
        if i>=z:
            continue
        if i<=x:
            z,y,x=y,x,i
        elif i<=y:
            z,y=y,i
        elif i<=z:
            z=i
    for i in map(int,s[n:].split()):
        if i>=z:
            continue
        if i<=x:
            z,y,x=y,x,i
        elif i<=y:
            z,y=y,i
        elif i<=z:
            z=i
    print(x+y+z)