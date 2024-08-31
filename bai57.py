# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:47:20 2024

@author: ASUS
"""

class SinhVien:
    def __init__(self, maSV, hoTen, GPA):
        self.maSV = maSV
        self.hoTen = hoTen
        self.GPA = GPA
        self.xepLoai = self.getXepLoai()

    def getXepLoai(self):
        if self.GPA < 3.5:
            return "Kém"
        elif 3.5 <= self.GPA < 5.0:
            return "Yếu"
        elif 5.0 <= self.GPA < 7.0:
            return "Trung bình"
        elif 7.0 <= self.GPA < 8.0:
            return "Khá"
        elif 8.0 <= self.GPA < 9.0:
            return "Giỏi"
        else:
            return "Xuất sắc"

    def __str__(self):
        return f"Mã SV: {self.maSV}, Họ tên: {self.hoTen}, GPA: {self.GPA}, Xếp loại: {self.xepLoai}"
import random

class QuanLySinhVien:
    def __init__(self):
        self.danhSachSV = []

    def themSinhVien(self, sv):
        self.danhSachSV.append(sv)

    def xuatDanhSach(self):
        for sv in self.danhSachSV:
            print(sv)

    def sinhVienCoDiemCaoNhat(self):
        return max(self.danhSachSV, key=lambda sv: sv.GPA)

    def timSinhVienTheoMa(self, maSV):
        for sv in self.danhSachSV:
            if sv.maSV == maSV:
                return sv
        return None

    def timSinhVienTheoDiem(self, diem):
        return [sv for sv in self.danhSachSV if sv.GPA == diem]

    def top10DiemCaoNhat(self):
        return sorted(self.danhSachSV, key=lambda sv: sv.GPA, reverse=True)[:10]

    def top10DiemThapNhat(self):
        return sorted(self.danhSachSV, key=lambda sv: sv.GPA)[:10]

    def khoiTaoNgauNhien(self, soLuong):
        for _ in range(soLuong):
            maSV = random.randint(1000, 9999)
            hoTen = f"Sinh viên {maSV}"
            GPA = round(random.uniform(3, 10), 2)
            sv = SinhVien(maSV, hoTen, GPA)
            self.themSinhVien(sv)
qlSV = QuanLySinhVien()

qlSV.khoiTaoNgauNhien(10)

qlSV.xuatDanhSach()

svCaoNhat = qlSV.sinhVienCoDiemCaoNhat()
print("Sinh viên có điểm cao nhất:", svCaoNhat)

svTimKiem = qlSV.timSinhVienTheoMa(1001)
if svTimKiem:
    print(svTimKiem)
else:
    print("Không tìm thấy sinh viên")

svDiem85 = qlSV.timSinhVienTheoDiem(8.5)
print("Các sinh viên có điểm 8.5:")
for sv in svDiem85:
    print(sv)

top10CaoNhat = qlSV.top10DiemCaoNhat()
print("Top 10 sinh viên có điểm cao nhất:")
for sv in top10CaoNhat:
    print(sv)