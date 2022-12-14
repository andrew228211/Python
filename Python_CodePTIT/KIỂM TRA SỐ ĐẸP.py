# def sholve(s):
#     for i in range(0,len(s)-2):
#         if(s[i]!=s[i+2]):
#             return "NO"
#     return "YES"
# for t in range(int(input())):
#     s=input()
#     print(sholve(s))
#     cnt=0
def sholve(s):
    for i in range(0,len(s)):
        if(s[i]!="0" and s[i]!="1"and s[i]!="2"):
            return "NO"
    return "YES"
for t in range(int(input())):
    s=input()
    print(sholve(s))
    cnt=0
    