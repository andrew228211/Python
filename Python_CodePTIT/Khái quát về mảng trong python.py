# Tạo 1 mảng
# a=[0]*10
# print(a)
# #thay đổi giá trị a[i]
# a[1]=2
# print(a)
# mảng 2 chiều
# a=[[0]*5]*3
# #thay đổi mảng
# # a[0][1]=2
# # print(a)
# # kết luận: thay đổi 1 giá trị trong mảng dẫn đến thay đổi tất cả các giá trị khác
# # nhưng nếu thay đổi 1 hàng thì vẫn được
# a[0]=[x for x in range(3)]
# print(a)
# a[1][2]+=1
# print(a)
#vì vậy nếu muốn thay đổi 1 giá trị của nó ta có thể dùng mảng như sau
a=[[0]*5 for x in range(3)]
print(a)
print("Sau khi thay doi gia tri thi mang se la")
a[1][2]=3
print(a)
#=> ta se thay doi duoc gia tri cua mang
#tương tự với mảng 3 chiều....