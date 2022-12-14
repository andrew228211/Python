text=[]
while(True):
    try:
        s=input().strip()
        s=s.capitalize()
        s=" ".join(s.split())
        l=len(s)
        if((s[l-1]=='!' or s[l-1]=='.' or s[l-1]=='?') and s[l-2]==" "):
            print(s[:(l-2)]+s[l-1])
        elif (s[l-1]=='!' or s[l-1]=='.' or s[l-1]=='?') and s[l-2].isalpha():
            print(s)
        else:
            s=s+'.'
            print(s)
    except:
        break
        