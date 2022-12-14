def thuannghich(n):
    str1=str(n)
    if(len(str1)<=1): return 0
    str2=str1[::-1]
    if(str1==str2):
        return 1
    return 0
t=int(input())
while(t>0):
    n=input()
    sum=0
    for i in n:
        sum=sum+int(i)
    if(thuannghich(sum)==1): print("YES")
    else: print("NO")
    t-=1