


# def thuannghich(n):
#     str1=str(n)
#     str2=str1[::-1]
#     if(str1==str2):
#         return 1
#     return 0
# def kiemtra(n):
#     s=str(n)
#     if(len(s)%2!=0): return 0
#     u=0
#     while n>0:
#         x=n%10
#         n=n//10
#         if(x%2!=0): return 0
#     return 1
# t=int(input())
# while(t>0):
#     n=int(input())
#     for i in range(22,n):
#         if(thuannghich(i)==1 and kiemtra(i)==1):
#             print(i,end=" ")
#     print()
#     t-=1    
    

a=[]
b=['0','2','4','8']
def Try(i):
    k=list(i)
    k=reversed()
    k=int(i+''.join(k))
    global a
    a=a+[k]
    if(len(i)!=3):
        for j in b:
            Try(j+i)
for i in range (1,5):
    Try(b[i])
a.sort()
for _ in range(int(input())):
    n=int(input())
    for j in a:
        if(j<n): print(j,end=" ")
        else: break
    print()