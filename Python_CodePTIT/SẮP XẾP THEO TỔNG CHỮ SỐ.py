from functools import cmp_to_key
import functools
def cmp(x,y):
    n=x
    m=y
    sum1=0
    sum2=0
    while(n>0):
        sum1+=n%10
        n=n//10
    while(m>0):
        sum2+=m%10
        m=m//10
    if(sum1==sum2):
        if x>y: return 1
        else : return -1
    elif sum1>sum2:
        return 1
    else: return -1
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input().split()]
    a = sorted(a, key = functools.cmp_to_key(cmp))
    for i in a:
        print(i,end=" ")
    print()
    