for _ in range(int(input())):
    s=input()
    lenght=len(s)
    l=s[0:(lenght//2)]
    r=s[(lenght//2):]
    xoay1=0
    for i in l:
        xoay1+=ord(i)-65
    while(xoay1>26):
        xoay1-=26
    tmpl=""
    tmpr=""
    for i in range(len(l)):
        tmp=xoay1+ord(l[i])-65
        if(tmp>=26):
            tmp=tmp-26
        tmpl+=chr(65+tmp)
    xoay2=0
    for i in r:
        xoay2+=ord(i)-65
    while(xoay2>=26):
        xoay2-=26
    for i in range(len(r)):
        tmp=xoay2+ord(r[i])-65
        if(tmp>26):
            tmp=tmp-26
        tmpr+=chr(65+tmp)
    ans=""
    for i in range(len(tmpr)):
        d=ord(tmpr[i])-65
        tmp=d+ord(tmpl[i])-65
        if(tmp>=26):
            tmp-=26
        ans+=chr(65+tmp)
    print(ans)
