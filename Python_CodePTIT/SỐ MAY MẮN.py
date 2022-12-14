s=input()
flag=0
cnt4=0
cnt7=0
for i in s:
   if(int(i)==4):
      cnt4+=1
   if(int(i)==7):
      cnt7+=1
print("YES" if(cnt4+cnt7==4 or cnt4+cnt7==7) else "NO")
