
ans=""
s=""
def check(res):
    global ans
    s1=int(res[0])*10+int(res[1])
    s2=int(res[5])*10+int(res[6])
    s3=int(res[10])*10+int(res[11])
    if(res[3]=='+'and s1+s2==s3):
        ans=res
    if(res[3]=='-'and s1-s2==s3):
        ans=res     
    if(res[3]=='*'and s1*s2==s3):
        ans=res       
    if(res[3]=='/'and s1/s2==s3 and s1%s2==0):
        ans=res     
def Back_Track(i,res):
    global ans
    if(ans!="WRONG PROBLEM"):
        return 
    if(i==len(s)):
        check(res)
        return
    if(s[i]=='?'):
        if(i==3):
            Back_Track(i+1,res+'+')
            Back_Track(i+1,res+'-')
            Back_Track(i+1,res+'*')
            Back_Track(i+1,res+'/')
        elif (i==0 or i==5 or i==10):
            for j in range(1,10):
                Back_Track(i+1,res+str(j))
        else:
            for j in range(10):
                Back_Track(i+1,res+str(j))
    else:
        Back_Track(i+1,res+s[i])
for _ in range(int(input())):
    s=input()
    ans="WRONG PROBLEM"
    Back_Track(0,"")
    print(ans)