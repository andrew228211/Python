n=int(input())
a=list(map(int,input().split()))
res =0
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
      if i<j and a[i]>a[j]:
        res+=1
print(res)