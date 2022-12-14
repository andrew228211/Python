class Data :
    def __init__(self, x, y):
        self.x = x
        self.y = y

t = int(input())
for z in range(t):
    n = int(input())
    a, q = [-1] * 110, []
    x, y, z = [int(i) for i in input().split()]
    q.append(Data(0, 0))
    a[0] = 0
    while len(q) > 0 :
        u = q[-1]
        q.pop()
        if u.x + 1 <= 101 and (a[u.x + 1] == -1) :
            a[u.x + 1] = a[u.x] + x
            q.append(Data(u.x + 1, u.y + x))
        if u.x - 1 > 0 and (a[u.x - 1] == -1 or a[u.x - 1] > u.y + y) :
            a[u.x - 1] = a[u.x] + y
            q.append(Data(u.x - 1, u.y + y))
        if u.x * 2 <= 101 and (a[u.x * 2] == -1 or a[u.x * 2] > u.y + z) :
            a[u.x * 2] = a[u.x] + z
            q.append(Data(u.x * 2, u.y + z))
    print(a[n])   
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     Min=[0]*100000
#     x, y, z = [int(i) for i in input().split()]
#     Min[1]=x
#     for i in range(2,n+1):
#         if(i%2==0):
#             Min[i]=min(Min[i-1]+x,Min[i//2]+z)
#         else:
#             Min[i]=min(Min[i-1]+x,Min[(i+1)//2]+z+y)        
#     print(Min[n])