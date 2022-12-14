# import re
# text=""
# for _ in range(int(input())):
#     s=input()
#     text+=s+" "
# regex="[\w]+"
# a=re.findall(regex,text)
# m={}
# for i in a:
#     i=i.lower()
#     if i in m:
#         m[i]+=1
#     else:
#         m[i]=1
# m=sorted(m.items(),key=lambda x:(-x[1],x[0]))
# for i in m:
#     print(i[0],i[1])
s1=""
a=[]
for _ in range(int(input())):
    s=input().lower()+' '
    tmp=""
    for i in range(len(s)):
        if((s[i]>='a' and s[i]<='z') or (s[i]>='A' and s[i]<='Z') or (s[i]>='0' and s[i]<='9')):
            tmp+=s[i]
        else:
            if s[i]!='':
                a.append(tmp)
                tmp=""
                
m={}
for i in a:
    if i in m and i!='':
        m[i]+=1
    elif i!='':
        m[i]=1
m=sorted(m.items(),key=lambda x:(-x[1],x[0]))
for i in m:
    print(i[0],i[1])