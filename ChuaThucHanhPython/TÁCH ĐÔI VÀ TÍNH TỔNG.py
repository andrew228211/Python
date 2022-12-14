s=input()
while(len(s)>1):
    tong=int(s[0:(len(s)//2)])+int(s[(len(s)//2):])
    s=str(tong)
    print(tong)
    