class Team:
    def __init__(self,ma,ten,truong):
        self.ma=ma
        self.ten=ten
        self.truong=truong
class ThiSinh:
     def __init__(self,ma,ten,maTeam):
        self.ma=ma
        self.ten=ten
        self.maTeam=maTeam
a=[]
b=[]
for i in range(int(input())):
    ma="Team"+"{:02d}".format(i+1)
    ten=input()
    truong=input()
    a.append(Team(ma,ten,truong))
for i in range(int(input())):
    ma="C"+"{:03d}".format(i+1)
    ten=input()
    maTeam=input()
    b.append(ThiSinh(ma,ten,maTeam))
b.sort(key=lambda X:X.ten)
for i in b:
    for j in a:
        if i.maTeam==j.ma:
            print(i.ma,i.ten,j.ten,j.truong)
            break    