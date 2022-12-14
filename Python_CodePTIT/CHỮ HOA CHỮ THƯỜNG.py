from tokenize import String
s=input()
dt=0
dh=0
for i in s:
    if(i>='A'and i<='Z'): 
        dh=dh+1
    elif(i>='a'and i<='z'): dt=dt+1
print(s.upper() if(dt<dh) else s.lower())