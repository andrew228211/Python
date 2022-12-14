#6=1+2+3
#9=4+5 2+3+4
#y tuong so cap*tong (dau+cuoi)=2n
from cmath import sqrt


for _ in range(int(input())):
    n=int(input())
    n=n*2
    cnt=0
    for i in range(2,int(sqrt(n).real)+1):
        if(n%i==0):
            tong=n//i
            if(tong-i)%2!=0:
                cnt+=1
    print(cnt)