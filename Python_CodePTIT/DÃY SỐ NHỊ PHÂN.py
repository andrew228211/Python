from itertools import combinations, permutations
n=int(input())
s=list(map(int,input().split()))
cnt=0
f=[]
for i in range(1,len(s)):
   if(s[i]!=s[i-1]): cnt+=1
print(cnt)