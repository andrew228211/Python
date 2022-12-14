import re
tu=""
for _ in range(int(input())):
    s=input()
    tu+=s+" "
regex=r"[\w]+"
x=re.findall(regex,tu)
m={}
for i in x:
    i=i.lower()
    if i in m:
        m[i]+=1
    else:
        m[i]=1
ds=sorted(m.items(),key=lambda X:(-X[1],X[0]))
for i in ds:
    print(i[0],i[1])