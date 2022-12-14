# import math
# t=int(input())
# while(t>0):
#     n=int(input()) 
#     if(n==1): print(1)
#     else:
#         print("1 *",end=" ")
#         s=""
#         for i in range(2,n+1):
#             cnt=0
#             while(n%i==0):
#                 cnt+=1
#                 n=n//i
#             if(cnt!=0):
#                 s=s+str(i)+"^"+str(cnt)+" * "
#         for i in range(0,len(s)-2):
#             print(s[i],end="")
#         print() 
#     t-=1
def solve():
    n = int(input())
    cnt = 0
    s = "1"
    for i in range(2,n):
        if n % i == 0:
            while n % i == 0:
                cnt += 1
                n = n/i
            s = s + " * " + str(i) + "^" + str(cnt)
            cnt = 0
    if n != 1:
        s = s + " " + str(n) + "^" + "1"
    print(s)

test = int(input())
while test >= 1:
    solve()
    test -= 1