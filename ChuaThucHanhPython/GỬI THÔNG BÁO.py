for _ in range(int(input())):
    s=input()
    try:
        if(s[99]!=" " and s[100]==" "):
            print(s[0:100])
        elif s[99]!=" " and s[100]!=" ":
            cnt=0
            for i in range(99,0,-1):          
                if(s[i]==" "):
                     cnt=i
                     break
            print(s[0:cnt])
        elif s[99]==" ":
           print(s[0:100])
    except:
        print(s)