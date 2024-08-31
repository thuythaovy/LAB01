# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:56:00 2024

@author: ASUS
"""

class NhanVien:
    def __init__(self, ma_nv, ho_ten, loai_nv, luong_co_ban, so_ngay_lam_viec=0, so_san_pham_ban=0):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.loai_nv = loai_nv
        self.luong_co_ban = luong_co_ban
        self.so_ngay_lam_viec = so_ngay_lam_viec
        self.so_san_pham_ban = so_san_pham_ban

    def tinh_luong(self):
        if self.loai_nv == "van_phong":
            return self.luong_co_ban + self.so_ngay_lam_viec * 150000
        else:
            return self.luong_co_ban + self.so_san_pham_ban * 18000

    def __str__(self):
        return f"Mã NV: {self.ma_nv}, Họ tên: {self.ho_ten}, Loại NV: {self.loai_nv}, Lương cơ bản: {self.luong_co_ban}, Lương: {self.tinh_luong()}"
import random

class QuanLyNhanVien:
    def __init__(self):
        self.danh_sach_nhan_vien = []

    def them_nhan_vien(self, nhan_vien):
        self.danh_sach_nhan_vien.append(nhan_vien)

    def xuat_danh_sach(self):
        for nv in self.danh_sach_nhan_vien:
            print(nv)

    def tim_theo_ma(self, ma_nv):
        for nv in self.danh_sach_nhan_vien:
            if nv.ma_nv == ma_nv:
                return nv
        return None

    def tim_nhan_vien_luong_cao_nhat(self):
        return max(self.danh_sach_nhan_vien, key=lambda nv: nv.tinh_luong())

    def tim_nhan_vien_ban_hang_luong_thap_nhat(self):
        nhan_vien_ban_hang = [nv for nv in self.danh_sach_nhan_vien if nv.loai_nv == "ban_hang"]
        if nhan_vien_ban_hang:
            return min(nhan_vien_ban_hang, key=lambda nv: nv.tinh_luong())
        else:
            return None

    def khoi_tao_ngau_nhien(self, so_luong):
        for _ in range(so_luong):
            ma_nv = f"NV{random.randint(1000, 9999)}"
            ho_ten = f"Nhân viên {ma_nv}"
            loai_nv = random.choice(["van_phong", "ban_hang"])
            luong_co_ban = random.randint(5000000, 10000000)
            if loai_nv == "van_phong":
                so_ngay_lam_viec = random.randint(20, 25)
            else:
                so_san_pham_ban = random.randint(100, 200)
            nv = NhanVien(ma_nv, ho_ten, loai_nv, luong_co_ban, so_ngay_lam_viec, so_san_pham_ban)
            self.them_nhan_vien(nv)
