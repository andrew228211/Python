#set trong python la 1 tap gia tri khong co thu tu
#gia tri trong set khong lap lai va khong the thay doi gia tri trong set
set1={1}
print(set1)
#Các giá trị trong set không có vị trí cố định nên không dùng được vị trí của nó
# dùng For
set1.add(3)
for i in set1:
    print(i,end=" ")
print()
#Cách sắp xếp theo thứ tự là dùng sorted
set1=sorted(set1)
print(set1)