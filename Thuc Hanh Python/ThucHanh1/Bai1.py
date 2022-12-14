def kt(n):
    for x in range(len(n)):
        if(n[x]!="4" and n[x]!="7"):
            return "NO"
    return "YES"
t=int(input())
for _ in range(t):
    n=input()
    print(kt(n))