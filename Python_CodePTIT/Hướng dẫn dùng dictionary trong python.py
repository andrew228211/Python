#dùng dic giống như dùng map trong c++ có 2 giá trị là key : value
# a={}
# for i in range(5):
#     a[i]=1
# print(a)
# kết quả: {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}
#ví dụ dùng map trong liệt kê số làn xuất hiện
a={1:5,2:4,3:6}
print(a)
# Chạy các Key (1,2,3) của a
for x in a:
    print(x,a[x])
#hoặc muốn lấy giá trị trong điều kiện phải đúng các key:
print(a.get(0))
#trả về các values
print(a.items())
#trả về các key
print(a.keys())
#tăng giá trị của key =1 lên 6
print(a[1])
a[1]+=1
print("sau khi tang la  %d"%(a[1]))
m={"Hoa":"Hong","Thua":"em"}
x=m["Hoa"]
print(x)