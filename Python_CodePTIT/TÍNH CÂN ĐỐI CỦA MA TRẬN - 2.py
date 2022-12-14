n=int(input())
a=[[]]*n
for i in range(n):
    a[i]=[int(x) for x in input().split()]
k=int(input())
s1 = 0
s2 = 0
for i in range(n) :
    for j in range(n) :
        if n-i-1 < j :
             s1 += a[i][j]           
        elif n-i-1>j:          
            s2 += a[i][j]
s = abs(s1 - s2)
if s <= k : print("YES")
else : print("NO")
print(s)