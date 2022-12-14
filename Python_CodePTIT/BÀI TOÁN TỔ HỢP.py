from itertools import combinations, combinations_with_replacement
n,k=map(int,input().split())
x=set(list(map(int,input().split())))
a=[]
for i in x:
    a.append(i)
res=list(combinations(a,k))
for i in res:
    for j in i:
        print(j,end=" ")
    print()
# m = {}
# n, k = [int(x) for x in input().split()]
# a = [int(x) for x in input().split()]
# b = [0] * (k + 1)
# for i in a :
#     m[i] = 1
# a = sorted(list(m))
# n = len(a)

# def Try(p) :
#     if p == k :
#         for i in range(1, k + 1) : print(a[b[i] - 1], end = " ")
#         print()
#         return
#     for i in range(b[p] + 1, n + 1) :
#         b[p + 1] = i
#         Try(p + 1)

# Try(0)