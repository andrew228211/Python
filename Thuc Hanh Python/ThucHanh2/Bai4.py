s=input()
a={int(s[0])*10+int(s[1])}
s=s[2:]
while(len(s)>1):
    if(len(s)%2)==0:
        a.add(int(s[0])*10+int(s[1]))
        s=s[2:]
    else:
        if(len(s)>2):
            a.add(int(s[0])*10+int(s[1]))
            s=s[2:]      
a=sorted(a)
for i in a:
    print(i,end=" ")