from math import gcd


n,m=map(int,input().split())
for i in range(n,m+1):
    for j in range(i+1,m+1):
        for k in range(j+1,m+1):
            if(gcd(i,j)==1 and gcd(j,k)==1 and gcd(i,k)==1):
                print("({0}, {1}, {2})".format(i,j,k))