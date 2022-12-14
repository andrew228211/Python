t=int(input())
while t>0:
    t-=1
    s=input().split(" ")
    a=int(s[0])
    b=int(s[1])
    if b==1:
        if a<=19:
            print("Ma Ket") 
        else:
            print("Bao Binh") 
    elif b==2:
        if a<=18:
            print("Bao Binh")
        else:
            print("Song Ngu")
    elif b==3:
        if a<=20:
            print("Song Ngu")      
        else:
            print("Bach Duong")
    elif b==4:
        if a<=19:
            print("Bach Duong")
        else:
            print("Kim Nguu")
    elif b==5:
        if a<=20:
            print("Kim Nguu")
        else:
            print("Song Tu")
    elif b==6:
        if a<=20:
            print("Song Tu")
        else:
            print("Cu Giai")
    elif b==7:
        if a<=22:
            print("Cu Giai")
        else:
            print("Su Tu")
    elif b==8:
        if a<=22:
            print("Su Tu")
        else:
            print("Xu Nu")
    elif b==9:
        if a<=22:
            print("Xu Nu")
        else:
            print("Thien Binh") 
    elif b==10:
        if a<=22:
            print("Thien Binh")
        else:
            print("Thien Yet")
    elif b==11:
        if a<=22:
            print("Thien Yet")
        else:
            print("Nhan Ma")             
    elif b==12:
        if a<=21:
            print("Nhan Ma")
        else:
            print("Ma Ket")