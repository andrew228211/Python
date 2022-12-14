class NhanVien:
    def __init__(self, ten, tuoi, dia_chi, tien_luong):
        self.ten = ten
        self.tuoi = tuoi
        self.dia_chi = dia_chi
        self.tien_luong = tien_luong
    def show (self):
        print("Tên:{0}, Tuổi: {1} , Địa chỉ: {2}, Quê quán: {3} ".format(self.ten, self.tuoi, self.dia_chi, self.tien_luong))
nv1 = NhanVien ("Hà Linh", 20, "Hải Dương", 3000000)
nv1.show()
bonus_money=0
t=int(input("Nhập số giờ làm của NV: "))
if t >= 200:
  bonus_money = nv1.tien_luong * 0.2
elif t < 100:
  bonus_money = 0
else:
  bonus_money = nv1.tien_luong * 0.1
print("Tiền thưởng nhân viên là: ", bonus_money)