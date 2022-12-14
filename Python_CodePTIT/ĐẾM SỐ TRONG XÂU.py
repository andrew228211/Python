# for i in range(int(input())):
#     s=input()
#     n=input()
#     print(s.count(n))
from math import gcd

#Số nguyên lớn
for i in range(int(input())):
    s=int(input())
    n=int(input())
    print(gcd(s,n))