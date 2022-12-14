from cmath import sqrt


def kt(n):
    if n<2:
        return 0
    for i in range(2,int(sqrt(n).real)+1):
        if(n%i==0):
            return 0
    return 1
for _ in range(int(input())):
    s=input()
    sum=0
    for x in s:
        sum+=int(x)
    if(kt(sum)==0):
        print("NO")
    else:
        print("YES")