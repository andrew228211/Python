#Tạo string
string1="Hoc bai di"
print(string1)
#doc tung ki tu
for x in range(len(string1)):
    print(string1[x])
#đọc từ dưới về đầu thì ô cuối là -1 lùi dần
# ví dụ
print(string1[-1])
#hoặc 
print(string1[-5])
#Đọc trong khoảng thì dùng như sau
print(string1[1:7])
#đọc ngược chuỗi 
print(string1[::-1])
#join là nối tất cả các chuỗi lại thành 1 chuỗi
s=("Sap","thi","roi")
print(" ".join(s))
ss="A+ ne" #chuỗi để nối các chuỗi  của s
print(ss.join(s))
#có thể đảo chuỗi bằng join và hàm đảo ngược có sẵn
print("".join(reversed(string1)))
#format 
x="{0:b}".format(16)
print("Binary: ",x)
#find tìm vị trí của từ trong chuỗi đã cho
s="AI buh v haha"
print(s.find("I"))
#capitalize: kí tự đầu tiên viết hoa còn lại viết thường
x="kHO"
print(x.capitalize())
#replace thay đổi kí tự trong chuỗi
x=x.replace("H","T")
print(x)