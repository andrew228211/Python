s1=input()
s2=input()
m={}
a={""}
b={""}
for i in s1.split():
    i=i.lower()
    if not i in m:
        m[i]=1
        b.add(i)
for i in s2.split():
    i=i.lower()
    if i in m:
        a.add(i)
    else:
        b.add(i)
a=sorted(a)
b=sorted(b)
for x in b:
    print(x,end=" ")
print()
for i in a:
    print(i,end=" ")