s = input()
while len(s) > 1 :
    s = str(int(s[0:(len(s) // 2)]) + int(s[(len(s)//2):]))
    print(s)
