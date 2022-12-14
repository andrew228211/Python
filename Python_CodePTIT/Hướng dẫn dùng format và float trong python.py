x=55
print("So la",x)
#Dạng số nguyên
print("So la %d"%x)
#lấy 2 số thập phân
print("So la %.2f"%x)
#hoặc dùng format
print("So la {:.2f}".format(x))
# cách viết số có 3 chữ số là:
y=80
for i in range(12):
    y=y+i
    print("{:03d}".format(y))
#format
print("Khi nao troi {0}, Toi di hoc {1} lan".format("mua",2))