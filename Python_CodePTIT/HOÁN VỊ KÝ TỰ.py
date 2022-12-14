from itertools import combinations, permutations
s=input()
res=list(permutations(s,len(s)))
for i in res:
    for j in i:
        print(j,end='')
    print()