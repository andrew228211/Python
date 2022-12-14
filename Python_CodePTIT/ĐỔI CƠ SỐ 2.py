def kt(s,base):
    if(len(s)%2!=0):
        s="0"+s
    for i in range(0,len(s)-1,2):
        res=s[i]+s[i+1]
        c=int(res,2)
        print(c,end='')
    return

def solve():
    base=int(input())
    num2 = input()
    num=int(num2,2)
    if base == 2:
        print(bin(num).replace("0b", ""))
    elif base == 4:
        kt(num2, 4)
        print()
    elif base == 8:
        print(oct(num).replace("0o", ""))
    elif base == 10:
        print(num)
    else:
        print(hex(num).replace("0x", "").upper())
t=int(input())
while(t>0):
    solve()
    t=t-1