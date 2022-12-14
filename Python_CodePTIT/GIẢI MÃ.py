t=int(input())
while t>0:
    s=input()
    j=0
    for i in range(1,len(s),2):
        j=0
        while(j<int(s[i])):
            print(s[i-1],end='')
            j=j+1
    print()
    t=t-1